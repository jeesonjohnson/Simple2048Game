import random
import copy
import pyfiglet as ascii
class GameBoard():
    def __init__(self):
        self._board=[["8","#","#","#"],["8","#","#","#"],["#","#","#","#"],["#","#","#","#"]]
        self._positions=[]
        self.update_available_positions()
        self.generate_random_number()
        self.update_available_positions()
        self.generate_random_number()
        self.highest_number=0

    def __str__(self):
        main_string=""
        string_gap=len(str(self.highest_number))-1
        for y in range(len(self._board[0])):
            for x in range(len(self._board)):
                if(len(str(self._board[x][y]))<len(str(self.highest_number))):
                    main_string+=  " | " +str(" "*string_gap) + str(self._board[x][y])+str(" "*string_gap)
                else:
                    main_string+= " | "+str(" "*string_gap) + str(self._board[x][y])
            main_string+=" |\n"
        return main_string

    def print_board(self):
        main_string=""
        string_gap=len(str(self.highest_number))-1
        for y in range(len(self._board[0])):
            for x in range(len(self._board)):
                if(len(str(self._board[x][y]))<len(str(self.highest_number))):
                    main_string+=  " | " +str(" "*string_gap) + str(self._board[x][y])+str(" "*string_gap)
                else:
                    main_string+= " | "+str(" "*string_gap) + str(self._board[x][y])
            main_string+=" |\n"
        return main_string

    def update_available_positions(self):
        self._positions=[]
        for y in range(len(self._board)):
            for x in range(len(self._board[0])):
                if(self._board[x][y]=="#"):
                    self._positions.append((x,y))

    def generate_random_number(self):
        self.chosen_number=[2,2,2,4][random.randint(0,4)-1]
        if(len(self._positions)!=0):
            self.chosen_position=self._positions[random.randint(0,len(self._positions)-1)]
            self._board[self.chosen_position[0]][self.chosen_position[1]]=str(self.chosen_number)
            self.update_available_positions()
            return True
        else:
            return False

    def upward_board_translation(self):
        for y in range(len(self._board)):
            for x in range(len(self._board[0])):
                if(y==0):
                    continue
                elif(self._board[x][y]!="#"):
                    yCounter=0
                    while True:
                        if(y-yCounter==0):
                            break
                        if(self._board[x][y-yCounter-1]=="#"):
                            self._board[x][y-yCounter-1]=self._board[x][y-yCounter]
                            self._board[x][y-yCounter]="#"
                            yCounter=yCounter+1
                        else:
                            if(self._board[x][y-yCounter-1]==self._board[x][y-yCounter]):
                                self._board[x][y-yCounter-1]=str(int(self._board[x][y-yCounter])*2)
                                self._board[x][y-yCounter]="#"
                                if(int(self._board[x][y-yCounter-1])>self.highest_number):
                                    self.highest_number=int(self._board[x][y-yCounter-1])
                            else:
                                break

    def rotate_array(self,array):
        temp_board=copy.deepcopy(self._board)
        for x in range(len(self._board)):
            for y in range(len(self._board[0])):
                temp_board[len(self._board)-1-y][x]=self._board[x][y]
        return temp_board
        



    def user_input(self,userInput):
        if(userInput=="UP" or userInput=="U"):
            self.upward_board_translation()
            return True
        elif(userInput=="DOWN" or userInput=="D"):
            self._board=self.rotate_array(self._board)
            self._board=self.rotate_array(self._board)
            self.upward_board_translation()
            self._board=self.rotate_array(self._board)
            self._board=self.rotate_array(self._board)

            return True
        elif(userInput=="LEFT" or userInput=="L"):
            self._board=self.rotate_array(self._board)
            self.upward_board_translation()
            self._board=self.rotate_array(self._board)
            self._board=self.rotate_array(self._board)
            self._board=self.rotate_array(self._board)
            return True
        elif(userInput=="RIGHT" or userInput=="R"):
            self._board=self.rotate_array(self._board)
            self._board=self.rotate_array(self._board)
            self._board=self.rotate_array(self._board)
            self.upward_board_translation()
            self._board=self.rotate_array(self._board)
            return True
        else:
            return False

    def check_win(self):
        if(self.highest_number=="2048"):
                return "WON"
        elif(len(self._positions)!=0):
            return "CONTINUE"
        else:
            self.original_board=copy.deepcopy(self._board)
            self.original_board_string=copy.deepcopy(self.print_board())
            self.operations=["LEFT","RIGHT","DOWN","UP"]
            for x in self.operations:
                self.user_input(x)
                if(self.original_board_string!=self.print_board()):
                    self._board=copy.deepcopy(self.original_board)
                    return "CONTINUE"
            self._board=copy.deepcopy(self.original_board)
            return "LOST"                


    def main(self):
        print(self.print_board())
        print(ascii.figlet_format("Welcome to the best 2048 game! :)"))
        print("The game works by typing either Left, Right, Up and Down, to join the numbers to get to 2048")
        self.temp=input("Ready? Press enter to begin")
        while True:
            print("\n"*30)
            print(self.print_board())
            print("Highest Number is :" +str(self.highest_number))
            self.user_choice=str(input("Choose either Left, Right, Up or Down!")).upper()
            if(self.user_input(self.user_choice)):
                self.update_available_positions()
                self.generate_random_number()
                self.win_value=self.check_win()
                if(self.win_value=="WON"):
                    print(ascii.figlet_format("YOU BEAT THE GAME WELL DONE!!"))
                    print("You won")
                    break
                elif(self.win_value=="LOST"):
                    print(ascii.figlet_format("Unfortunately you lost :("))
                    print("You Lost :(")
                    break
                else:
                    continue
            else:
                print("Sorry that did not register make sure you choose between Left, Right, Up or Down!")
                continue
        print(ascii.figlet_format("THANK YOU FOR PLAYING"))

        self.play_again=str(input("\n\nWant to play again? (Y/N)")).upper()
        if(self.play_again=="Y" or self.play_again=="YES"):
            self.main()
        else:
            print("Okay see ya later :)")


if __name__ == "__main__": 
    game_object=GameBoard()
    game_object.main()