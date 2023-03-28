from twilio.rest import Client
sid='ACf11b41614176d0ff50d0f461903023df'
authToken='56d9c3aede60d375baa1bfdd5291c98a'
client=Client(sid,authToken)

message=client.messages.create(to='whatsapp:+254114241129',
                               from_='whatsapp:+14155238886',
                               body='hey simon do you want to withdraw,deposit or send money',)