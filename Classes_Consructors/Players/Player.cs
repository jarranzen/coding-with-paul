using System;
namespace Classes_Consructors.Player
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
            Console.WriteLine("Hi my name is " + Name + " and my age is " + Age);
        }
    }
} 