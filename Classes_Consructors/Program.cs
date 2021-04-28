using System;
using Classes_Consructors.Player;


namespace Classes_Consructors
{
   
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Player attributes 
           Player player1 = new Player();
            player1.Name = "John";
            player1.Age = 28;
            player1.HasPet = true;
            player1.IsDead = false;

            player1.Greeting();


            Player player2 = new Player();
            player2.Name = "Jane";
            player2.Age = 52;
            player2.HasPet = false;
            player2.IsDead = false;

            player2.Greeting();



            
        }
    }
