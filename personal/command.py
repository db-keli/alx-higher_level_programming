#!/usr/env python
import cmd
import os


class Prompt(cmd.Cmd):
    
    last_output = ''
    
    def do_welcome(self, person):
        print(f"Hello, {person}")
    
    
    def help_welcome(self, line):
        print ('\n'.join([ 'greet [person]',
                            'Greet the named person',
                          ]))
        
        
    def do_EOF(self):
        return True
    

    def do_shell(self, line):
        "Run shell command"
        print("running shell command:", line)
        output = os.popen(line).read()
        print (output)        

    
if __name__ == '__main__':
    Prompt().cmdloop()
