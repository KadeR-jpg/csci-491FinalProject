import re # regexes to make string item replacement a bit easier
import string
tag_re = "(<[A-z]+>)" # This regex allows for easy filtering of tags so we can replace them without too much trouble

supported_types = {'noun':0,'verb':0,'adverb':0,'pnoun':0,'pronoun':0,'adjective':0}

sample_input = "Jimmy the <noun> was an <adjective> type of <pronoun>, with an <adjective> <noun> made out of many <noun>"

full_sample = "bird,eggplant,tomato seed||||gremlin|small,green"

full_user_sample = "noun1,noun2|verb1|adverb1,adverb2|pnoun1,pnoun2|pronoun1|adjective1,adjective2"

''' 
^^ make sure the string of inputs follows that template when pushed to the db
that might need to be in JS so we can more easily get the field values from the form
'''

class MLGen():

    def __init__(self):
        self.noun_indices = []
        self.verb_indices = []
        self.adverb_indices = []
        self.pnoun_indices = []
        self.pronoun_indices = []
        self.adjective_indices = []


        # these will individually need to be pushed to the db
        self.noun_count = 0
        self.verb_count = 0
        self.adverb_count = 0
        self.pnoun_count = 0
        self.pronoun_count = 0
        self.adjective_count = 0

        self.safe_indices = ''

        self.template = ''

    # I'm pretty much using this as a switch statement to handle all of the different supported word types
    def word_handler_handler(self,w_index,word):
        def handle_noun(w_index):
            print("we are handling a noun")
            supported_types["noun"] +=1
            self.noun_indices.append(w_index)
        def handle_verb(w_index):
            print("we are handling a verb")
            supported_types["verb"] +=1
            self.verb_indices.append(w_index)
        def handle_adverb(w_index):
            print("we are handling an adverb")
            supported_types["adverb"] +=1
            self.adverb_indices.append(w_index)
        def handle_pnoun(w_index):
            print("we are handling a proper noun")
            supported_types["pnoun"] +=1
            self.pnoun_indices.append(w_index)
        def handle_pronoun(w_index):
            print("we are handling a pronoun")
            supported_types["pronoun"] +=1
            self.pronoun_indices.append(w_index)
        def handle_adjective(w_index):
            print("we are handling an adjective")
            supported_types["adjective"] +=1
            self.adjective_indices.append(w_index)
        locals()['handle_' + word](w_index)
        

    '''Takes all of the word type indices and puts them into a single string that we can use in the DB
        I'm sure there's a better way to do that, but this will work for now. I'm no database expert'''
    def make_DB_safe_counters(self):
        comp_list = "" #this holds the indices
        comp_list += ','.join(list(map(str,self.noun_indices)))
        self.noun_count = len(self.noun_indices)
        comp_list += '|'

        comp_list += ','.join(list(map(str,self.verb_indices)))
        comp_list += '|'
        self.verb_count = len(self.verb_indices)

        comp_list += ','.join(list(map(str,self.adverb_indices)))
        comp_list += '|'
        self.adverb_count = len(self.adverb_indices)

        comp_list += ','.join(list(map(str,self.pnoun_indices)))
        comp_list += '|'
        self.pnoun_count = len(self.pnoun_indices)

        comp_list += ','.join(list(map(str,self.pronoun_indices)))
        comp_list += '|'
        self.pronoun_count = len(self.pronoun_indices)

        comp_list += ','.join(list(map(str,self.adjective_indices)))
        self.adjective_count = len(self.adjective_indices)

        return comp_list



    """ 
    Main parser functionality
    in_template: story template from the db
    """
    def gen_template(self,in_template):
        tokens = in_template.split(); # First we tokenize the string, to make the "parsing" easier
        ta = '' # definition of the re find object
        #print(temp)
        for ind in range(len(tokens)): # Step through all of the string tokens
            word = tokens[ind] # Grab the actual word
            #word = word.strip(',') # Remove punctuation (right now it's just commas. probably fine for the time being)
            ta = re.search(tag_re,word)
            if ta != None: # checks if the current token is a word tag
                #print("found a tag")
                word = ta.string
                word = word.strip(string.punctuation)
                for word_type in supported_types: # now check if the tag matches one of the currently supported word types
                    if word == word_type:
                        self.word_handler_handler(ind, word)

        self.safe_indices = self.make_DB_safe_counters()
        #TODO: push all of the counters to the DB (not much I could do here to simplify that table, sorry aobut that)

        return self.safe_indices

        #TODO: take that return value and push it to the DB


    def strList_to_intList(self,l):
        to_ret = []
        if len(l)>0:
            for item in l:
                if item != '':
                    to_ret.append(int(item))
        return to_ret


    """
    Takes user input and populates a template with those responses
    in_template: same as with gen_template
    user_responses: user input from the form on the story generator page. 
            Keep this formatted like full_user_sample at the top of this file.
    word_indices: the return value from gen_template

    """
    def pop_template(self,in_template, user_responses, word_indices):
        mod_template = in_template.split()

        # splits the word index array into arrays per word type
        word_indices = word_indices.split('|')
        word_indices = [i.split(',') for i in word_indices]
        noun_indices = self.strList_to_intList(word_indices[0])
        verb_indices = self.strList_to_intList(word_indices[1])
        adverb_indices = self.strList_to_intList(word_indices[2])
        pnoun_indices = self.strList_to_intList(word_indices[3])
        pronoun_indices = self.strList_to_intList(word_indices[4])
        adjective_indices = self.strList_to_intList(word_indices[5])

        # splits the user response array into separate arrays for each word type
        user_responses = user_responses.split('|')
        user_responses = [i.split(',') for i in user_responses]
        replacement_nouns = user_responses[0]
        replacement_verbs = user_responses[1]
        replacement_adverbs = user_responses[2]
        replacement_pnouns = user_responses[3]
        replacement_pronouns = user_responses[4]
        replacement_adjectives = user_responses[5]

        for ind in range(len(noun_indices)):
            mod_template[noun_indices[ind]] = re.sub(tag_re,replacement_nouns[ind],mod_template[noun_indices[ind]])

        for ind in range(len(verb_indices)):
            mod_template[verb_indices[ind]] = re.sub(tag_re,replacement_verbs[ind],mod_template[verb_indices[ind]])
            
        for ind in range(len(adverb_indices)):
            mod_template[adverb_indices[ind]] = re.sub(tag_re,replacement_adverbs[ind],mod_template[adverb_indices[ind]])

        for ind in range(len(pnoun_indices)):
            mod_template[pnoun_indices[ind]] = re.sub(tag_re,replacement_pnouns[ind],mod_template[pnoun_indices[ind]])

        for ind in range(len(pronoun_indices)):
            mod_template[pronoun_indices[ind]] = re.sub(tag_re,replacement_pronouns[ind],mod_template[pronoun_indices[ind]])

        for ind in range(len(adjective_indices)):
            mod_template[adjective_indices[ind]] = re.sub(tag_re,replacement_adjectives[ind],mod_template[adjective_indices[ind]])
        
        filled_story = ' '.join(mod_template)
        return filled_story # this can be used to populate the text field

        
        
        
        

#genny = MLGen()
#genny.gen_template(sample_input)
#print(genny.make_DB_safe_counters())
#print(genny.pop_template(sample_input,full_sample,genny.safe_indices))
