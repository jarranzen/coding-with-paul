using System;

namespace Classes_Consructors
{
    public class Player
    {
        // Set up the empty attributes to be filled

        public string Name;
        public int Age;
        public bool HasPet;
        public bool IsDead;


        public void Greeting()
        {
            Console.WriteLine("Hi my name is " + Name + " and my age is " + Age );
        }
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
}
