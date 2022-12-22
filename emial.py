def send_mail(mail,name):
    import smtplib
    import imghdr
    from email.message import EmailMessage

    Sender_Email = ""
    Reciever_Email = mail
    Password = ""
    newMessage = EmailMessage()
    newMessage['Subject'] = "Word Document"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('Here is your Image!')
    with open(name, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)
    print("Sent")
def sendMsg(mail,msg,sub):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    mail_content = msg
    sender_address = '*********@gmail.com'
    sender_pass = ''
    receiver_address = mail
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = sub  #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')



def sendpdf(mail,pdfname):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import smtplib
    import imghdr
    from email.message import EmailMessage


    sender = "***********@gmail.com"
    password = ''
    # put the email of the receiver here
    receiver = mail

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = "Here is your PDF"
    body="Hello "+str(mail).split("@")[0]+"!!!"
    message.attach(MIMEText(body, 'plain'))



    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    # use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)

    # enable security
    session.starttls()

    # login with mail_id and password
    session.login(sender, password)

    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent')



def sendword(mail,wordname):
    import smtplib

    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email import encoders
    sender = "***********@gmail.com"
    password = ''

    fromaddr = sender
    toaddr = mail

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Here is your word Document"

    body="Hello "+str(mail).split("@")[0]+"!!!"

    msg.attach(MIMEText(body))

    files = [wordname]

    for filename in files:
        attachment = open(filename, 'rb')

        part = MIMEBase("application", "octet-stream")

        part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header("Content-Disposition",
                        f"attachment; filename= {filename}")

        msg.attach(part)

    msg = msg.as_string()

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()
        print('Email sent successfully')
    except:
        print("Email couldn't be sent")
