import bashparse


def basic_node_unroll(nodes, function_dict = {}, command_alias_list={}):
	# Command substitutions are gonna be weird
	if type(nodes) is not list: nodes = [nodes]
	for node in nodes: 
		if type(node) is not bashparse.node: raise ValueError('nodes must be of type bashparse.node')
	unrolled_nodes = []

	for node in nodes: 
		if node.kind == 'compound':
			unrolled_nodes += basic_node_unroll(node.list, function_dict, command_alias_list)
		elif node.kind == 'for':
			if len(node.parts) > 4:
				command_nodes = bashparse.return_paths_to_node_type(node.parts[4:], 'command')
				for command in command_nodes:
					unrolled_nodes += basic_node_unroll(command.node, function_dict, command_alias_list)
		elif node.kind == 'if':
			unrolled_nodes += [ node ]
		elif node.kind == 'command':
			command_alias_list = bashparse.return_command_aliasing(node, command_alias_list)
			node = bashparse.replace_command_aliasing(node, command_alias_list)
			node = bashparse.replace_functions(node, function_dict)
			for itr in node:
				if itr.kind == 'compound': # ie function replacement happened
					unrolled_nodes += basic_node_unroll(itr.list, function_dict, command_alias_list)
				else:
					unrolled_nodes += [ itr ]
		elif node.kind == 'function':
			function_dict = bashparse.build_function_dictionary(node, function_dict)
		elif hasattr(node, 'parts'):
			unrolled_nodes += basic_node_unroll(node.parts)
		elif hasattr(node, 'list'):
			unrolled_nodes += basic_node_unroll(node.list)
	return unrolled_nodes




filename = './testing.sh'

nodes = bashparse.parse(open(filename).read())

function_dict = {}

var_list = {}

function_dict = bashparse.build_function_dictionary(nodes)
unrolled_nodes = bashparse.replace_functions(nodes, function_dict)
replaced_nodes = bashparse.substitute_variables(unrolled_nodes, var_list)
unrolled_nodes = basic_node_unroll(replaced_nodes)


for ast in unrolled_nodes:
	print(ast.dump())