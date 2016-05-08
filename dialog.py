#!/usr/bin/python

import json
from os.path import join, dirname
from watson_developer_cloud import DialogV1


def main():
	dialog = DialogV1(
	    username='eeccaad4-3cb0-4ab1-b3f2-e827abf95a93',
	    password='4CVJIoZZ2Qbi')

	print(dialog.get_dialogs()['dialogs'])
	#dialog.delete_dialog('5226a6ee-01ba-417b-840f-0215bf83457f')
	#print(json.dumps(dialog.get_dialog('6250d170-41d6-468a-a697-5675578c8012'), indent=2))
	#CREATE A DIALOG
	with open(join(dirname(__file__), 'raine.xml')) as dialog_file:
		dialog_id = dialog.create_dialog(dialog_file=dialog_file, name='heyraine')['dialog_id']

	with open(join(dirname(__file__), 'raine.xml')) as dialog_file:
		(dialog.update_dialog(dialog_file=dialog_file, dialog_id=dialog_id))

	#print(json.dumps(dialog.get_content(dialog_id), indent=2))
	initial_response = dialog.conversation(dialog_id)['response']
	
	print(initial_response)

	user_input = input("")	
	#print(dialog.conversation(dialog_id=dialog_id, dialog_input=user_input))
	conversation_id = dialog.conversation(dialog_id)['conversation_id']
	client_id=dialog.conversation(dialog_id)['client_id']

	next_response = dialog.conversation(dialog_id, user_input, client_id, conversation_id)['response']
	print(next_response)
	user_input = input("")
	next_response = dialog.conversation(dialog_id, user_input, client_id, conversation_id)['response']
	print(next_response)

	dialog.delete_dialog(dialog_id)
	#dialog.delete_dialog(dialog_id=dialog_id)	
	#print(json.dumps(dialog.delete_dialog(dialog_id='c05e2bf9-2fcd-4af5-8230-f95f91b4865c'), indent=2))

	# print(json.dumps(dialog.update_profile(
	#     dialog_id='6250d170-41d6-468a-a697-5675578c8012', client_id=123, name_values=[{'name': 'test', 'value': 'v1'}]),
	#     indent=2))
	#
	# print(json.dumps(dialog.get_profile(
	#     dialog_id='6250d170-41d6-468a-a697-5675578c8012', client_id=123), indent=2))


if __name__ == "__main__":

	main()
