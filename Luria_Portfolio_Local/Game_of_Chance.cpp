// Dice Game
// Programmer: David Luria

#include <iostream>
#include <cstdlib>

using namespace std;

bool playOneGame(int point){
    //Roll and display 3 random numbers 1-6
    int roll1 = rand() % 6 + 1;
    cout<<endl<<"Roll 1: "<<roll1<<endl;
    int roll2 = rand() % 6 + 1;
    cout<<"Roll 2: "<<roll2<<endl;
    int roll3 = rand() % 6 + 1;
    cout<<"Roll 3: "<<roll3<<endl;
    //Check if one of the rolls is a winner.
    if(point == roll1 || point == roll2 || point == roll3){
        cout<<"**You win!**"<<endl;
        return(true);
    }
    else{
        cout<<"**You lose!**"<<endl;
        return(false);
    }
}

void Display(double Balance){
    cout<<"You have $"<<Balance<<" in the bank." <<endl;
}

void winPercent(int wins, int losses){
    double percent;
    if((wins+losses) != 0){
        percent = 100 *(wins/(double(wins)+double(losses)));
    }
    else{
        percent = 0;
    }
    cout<<"You won "<<percent<<"% of your games!"<<endl;
}
    
int main(){
    srand(time(NULL));
    int point;
    int wins = 0;
    int losses = 0;
    double bank = 100;
    double wager;
    bool playagain;
    //loop game until user inputs 0 to exit
    do{
        Display(bank);
        do{
            cout<<"Choose your point (1-6), input 0 to exit: ";
            cin>>point;
            if(point>6 || point<0){
                cout<<"Invalid input"<<endl<<endl;
            }
            else if(point == 0){
                ;
            }
            ;
        }
        while((point > -1 && point < 7) == 0);
        //Exit if 0 is input
        if(point == 0){
            ;
        }
        else{
            //Ask for a wager. If 0, game will exit.
            do{
                cout<<"Enter wager (input 0 to exit game): ";
                cin>>wager;
                if(wager>bank){
                    cout<<endl<<"Insufficient funds."<<endl;
                }
                else if(wager<0){
                    cout<<endl<<"Wager must not be negative."<<endl;
                }
            }while(wager>bank || wager<0);
        }
        if(point == 0 || wager == 0){
            cout<<"Exiting..."<<endl;
        }
        //Play the game if a valid point and wager are chosen
        else{
            bool result = playOneGame(point);
            if(result == true){
                wins += 1;
                bank += wager;
            }
            else if(result == false){
                losses += 1;
                bank -=wager;
            }
            //If the bank has money in it, the game displays the win statistics 
            //and asks if the player wants to play again. If no money, it exits.
            if(bank>0){
                cout<<endl<<"Wins: "<<wins<<endl
                <<"Losses: "<<losses<<endl
                <<"Total Games: "<<wins+losses<<endl;
                //Displays balance
                Display(bank);
                //The game asks if the player wants to play again
                int response;
                do{
                    cout<<endl<<"Play again? 1 for yes, 0 for no. "<<endl;
                    cin>>response;
                    if(response !=0 && response !=1){
                        cout<<"Invalid input."<<endl;
                    }
                    else{
                        playagain = response;
                        cout<<endl;
                    }
                }while(response !=0 && response !=1);
            }
        }
    }
    while(point != 0 && wager != 0 && bank != 0 && playagain != 0);
    cout<<endl<<"***Game Over!***"<<endl
    <<"Wins: "<<wins<<endl
    <<"Losses: "<<losses<<endl
    <<"Total Games: "<<wins+losses<<endl;
    winPercent(wins, losses);
    Display(bank);
    return(0);
}