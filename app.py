from regex import search
from assembly import AssemblyAI
from rich import print

API_KEY = 'd05010b4cca14f31a8a7450db6ac3679'

ai1 = AssemblyAI(API_KEY)

media_file_path = '.\media\WhatsApp Ptt 2022-10-03 at 6.51.58 PM.mp3'
response_upload = ai1.upload_audio_by_file(media_file_path)
response_json_output = response_upload.json()
transcript_id = response_json_output['id']

response_status = ai1.retrieve_transcript(transcript_id)
print(response_status)
print(response_status['status'])
print(response_status['text'])