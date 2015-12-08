# Design

			     	Hawcha UI
		       		   /\
                      /  \      
                     /    \
                    /      \
           AppControl   Authentication
               /\            \
              /  \            \
             /    \            \
            /      \            \
          SMC	  Broadcast     User





##AppControl:

	getSmName()
		Input: None
		Output: Social Media name
		Specification: Read social media name from user.
		
	getSmUserName()
		Input: None
		Output:	Social media user name
		Specification: Read social media user name from user. 

	getSmUserPasswd()
		Input: None
		Output: Social media password
		Specification: Read social media password from user

	isInSocialMedia()
		Input: Social media name, SMC.displaySm()
		Output: Boolean
		Specification: Check if the given social media is in the added social media list.


	getMessage()
		Input: None
		Output: Message to broadcast
		Specification: Read the message from the user

	getSmList()
		Input: None
		Output: List of social media 
		Specification: Read the list of social media to broadcast from user.

##Authentification:

	getUserName()
		Input: None
		Output: User name
		Specification: Read the user name from user

	getUserPasswd()
		Input: None
		Output: Password
		Specification: Read the password from the user

##SMC:

	addSm()
		Input: getSmName(),getSmUserName(), getSmUserPasswd()
		Output: Boolean
		Specification: Add the given social media.
		
	rmSm()
		Input: getSmName()
		Output: Boolean
		Specification: Remove the given social media.
		
	displaySm()	
		Input: None
		Output: Social media list
		Specification:	Display the list of social media

##Broadcast:

	broadcastMessage()
		Input: getMessage(), getSmList() 
		Output: Boolean
		Specification: Broadcast the message to various social media

##User:

	addUser()
		Input: getUserName(), getUserPasswd() 
		Output: Boolean
		Specification: Add application user.
		
	rmUser()
		Input: getUserName(), getUserPasswd()
		Output: Boolean
		Specification: Remove user from the application
