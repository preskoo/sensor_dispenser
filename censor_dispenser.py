# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# fonction supprimant les mots interdits donnés
def censure(mot_interdit="learning algorithms", fichier=email_one):
	mot_censuré = "" #initialise le chaine de caractère
	for lettre in mot_interdit:
		if lettre != " ":	# remplace les mots mais pas les espaces
			mot_censuré += "X"
		else:
			mot_censuré += " "
		
	return fichier.replace(mot_interdit, mot_censuré)

# print(censure())

# exercice 2, censure un liste de mots
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def multicensor(censored_words = proprietary_terms, email2 = email_two):
	for word in censored_words:
		Xword = ""
		for letter in word:
			Xword += "X"
		email2 = email2.replace(word, Xword) #remarque : ne modifie pas le fichier (  car ouvert avec read() ??? )
	return email2
#print(multicensor())


# exercice 3
#The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”

# Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def occurences(neg_words = negative_words, email = email_three):
#bloucle pour un mot de la liste
	occurence = []
	item_occurence = []
	for item in neg_words:
		item_count = email.count(item)
		occurence.append(item_count)
		if item_count > 1 :
			i = len(item)
			Xword = "X"*i
			email = email.replace(item, Xword)
			
	item_occurence = list(zip(negative_words, occurence))
	return item_occurence, email
#print(occurences())



# exercice 4
#This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”

#Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.

#As a challenge, make sure they:

#    Handle upper and lowercase letters.
 #   Handle punctuation.
  #  Censor words while preserving their length.

censure_list = []
censure_list = negative_words + proprietary_terms
def super_censure(censure_list , email = email_four):
	ponctuation = [",", "!", "?", ".", "%", "/", "(", ")"]
	i = 0
	while i < len(email) :
		print(email[i])
		i += 1
				
#		
#
#
#
#
#
			


