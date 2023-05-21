class PromptProcessor:
                   
    def get_mode(self, input_string):
        if 'custom' in input_string:
            return 'custom'
        elif 'offline' in input_string:
            return 'offline'
        else:
            return None

    def get_source(self, input_string):
        words = input_string.split()
        mode = self.get_mode(input_string)
        if mode and mode in words:
            index = words.index(mode)
            if index < len(words) - 1:
                return words[index + 1]
        return None

    def get_prompt(self, input_string):
        mode = self.get_mode(input_string)
        source = self.get_source(input_string)
        words = input_string.split()
        if mode and source and (source in words):
            index = words.index(source)
            if index < len(words) - 1:
                return ' '.join(words[index + 1:])
        return None
    
    def process_request(self, input_string):
        mode = self.get_mode(input_string)
        print('mode selection :', mode)
        source = self.get_source(input_string)
        print('source selection :', source)

        actions = {
            ('custom', 'data'): 1,
            ('custom', 'text'): 2,
            ('custom', None): 0,
            ('offline', 'data'): 3,
            ('offline', 'text'): 4,
            ('offline', None): 0
        }

        result = actions.get((mode, source))
        return result