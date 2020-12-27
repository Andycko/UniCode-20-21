def get_recipient(message, position):
        # Your code goes here
        recipients = []
        allowedRange = list(range(48,58))
        allowedRange += list(range(65,91))
        allowedRange += list(range(97,123))
        allowedRange.append(95)
        allowedRange.append(45)

        while "@" in message:
            # loop while "@" is in the message
            originalIndex = message.index("@")
            index = originalIndex
            username = ""
            try:
                # this try-except block is for the chance when "@" is at the end of the message
                while ord(message[index + 1]) in allowedRange:
                    # while the next character after "@" is allowed in usernames
                    username += (message[index + 1])
                    index += 1
            except IndexError:
                break

            if(index != originalIndex):
                # if there are some valid characters in the username
                # remove the username from the message and add username to the recipients
                message = message.replace("@" + username, ' ')
                recipients.append(username)

            # if there are no characters in the username, ignore it and remove from message
            message = message[index + 1::]
            
        try:
            return recipients[position - 1]
        except IndexError:
            return ""

print(get_recipient("Hey @Joe_Bloggs what time are we meeting @_-@FredBloggs?", 2))