using System;
using System.Collections.Generic;

namespace Neighbourhood
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Classes for Room and House are defined, and custom print methods
             * for each are added. A couple of different means of defining rooms
             * are also shown.
             * 
             * 
             * TODO: Add method to calculate the area of any room in the house
             * TODO: Calculate area of house by adding up areas of rooms
             * TODO: Situate a house on a *Property* (which may have more than
                   one house on it. It might also have a pool, and a garden...
             * TODO: Rather than create the rooms inline, have them in a csv file
             *      and read that in, creating one room per row
             *      name, width, length, doors, windows, lights, carpetted
             */

            // First make some rooms to work with

            var bedroom1 = new Room(
                name: "Bedroom 1",
                width: 3.4,
                length: 4.1,
                doors: 2,
                windows: 3,
                lights: 1,
                carpetted: true
                );

            var bedroom2 = new Room(
                name: "Bedroom 2",
                width: 3.2,
                length: 4.8,
                doors: 1,
                windows: 2,
                lights: 2,
                carpetted: true
                );

            var kitchen1 = new Room(
                name: "Kitchen",
                width: 2.4,
                length: 3.1,
                doors: 2,
                windows: 1,
                lights: 4,
                carpetted: false
                );

            // Make a new list, consisting of the rooms made above

            var RoomList1 = new List<Room>
            {
                bedroom1,
                bedroom2,
                kitchen1
            };

            // Make a toilet to add later...

            var toilet = new Room(
                name: "Toilet",
                width: 2.0,
                length: 2.1,
                doors: 1,
                windows: 0,
                lights: 2,
                carpetted: false
                );

            // Add a light to kitchen1

            kitchen1.lights += 1 ;

            // Can we add the same room twice? Sure...
            RoomList1.Add(kitchen1);

            // (Note that "lights" is now 5 in both instances,
            // as they both point to the same object)

            // Now create a house that contains the rooms in RoomList1,
            // and a few attributes of its own

            var house1 = new House(
                rooms: RoomList1,
                address: "81 Childers St, North Adelaide",
                width: 8.0, // width of the *house*
                length: 15.9, // length of the *house*
                carparks: 1
                );

            // A text description of the house, assembled "by hand"

            Console.WriteLine($"Kitchen1: { kitchen1} \nBedroom1: { bedroom1} \nBedroom2: { bedroom2}");

            // Better to go through the list automatically, in case we add any
            // other rooms and forget to update the description...

            foreach (var room in house1.rooms)
            {
                Console.WriteLine(room);
            }

            // Or, better again, use the ToPrint() method defined below to "print a house"

            Console.WriteLine(house1);

            Console.WriteLine("Now extend the house by adding a toilet\n");

            house1.rooms.Add(toilet); // Nice and simple when the object is well-defined

            // You can also add a room "inline": that is, define it "within" the call
            // to Add() it to the list. 

            house1.rooms.Add(new Room(name: "Study", width: 2.3, length: 1.8, doors: 1,
                windows: 2, lights: 3, carpetted: true));

            Console.WriteLine("Print out the house after this extension\n");

            Console.WriteLine(house1);

        }
    }

    internal class House
    {
        public List<Room> rooms; // a litst of rooms
        private string address; // street address
        private double width; // house width in metres
        private double length; // house length in metres
        private int carparks; // number of car parks


        // Simple constructor for now...

        public House(List<Room> rooms, string address, double width, double length, int carparks)
        {
            this.rooms = rooms;
            this.address = address;
            this.width = width;
            this.length = length;
            this.carparks = carparks;
        }

        public override string ToString()  // How to print a House
        {
            string stringret = $"===================\nHouse at: {address}\n";
                foreach (var myroom in rooms)
            {
                stringret+=myroom;
            }
            return stringret + "===================\n";
        }
    }

    internal class Room  // A rectangular room 
    {
        private string name; // description of the room
        private double width; // width in metres
        private double length; // length in metres
        private int doors; // number of doors
        private int windows; // number of windows
        public int lights { get; set; } // allow new lights to be added/removed
        private bool carpetted; // true or false!

        public Room(string name, double width, double length, int doors, int windows, int lights, bool carpetted)
        {
            this.name = name;
            this.width = width;
            this.length = length;
            this.doors = doors;
            this.windows = windows;
            this.lights = lights;
            this.carpetted = carpetted;
        }

        public override string ToString()
        {
            // Note that we use "lights" if there's more than one of them and
            // "light" if there's only one below. Similarly with carpet.
            // It's a good trick to know. Play with the expressions inside
            // {(..)} at the end in the REPL if it's not clear what's happening

            return $"{name} is a {width} x {length} room with {lights} light{(lights>1?"s":"")}" +
                $"{(carpetted ? " and carpet" : " without carpet")}\n";
        }

    }
}


