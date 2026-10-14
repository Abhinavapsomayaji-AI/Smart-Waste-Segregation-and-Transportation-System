# Smart-Waste-Segregation-and-Transportation-System

## Inspiration💫:
The Inspiration for this is unlike "AIATSS" -my other project- is much less personal. It is a general problem in the world with waste management like sometimes in India, they dump waste in empty grounds, fields ,etc as there are no proper waste disposal system at a local level even if there is it struggles to keep up with the amount of trash that is being generated. I had similar thought of creating a Automatic waste segregation system long time ago but i never built a software like this. Initially for this system i thought of making this system for local use in everyday life but later i realised that is economically less feasable and it is hard to maintain. So for a solution I want this to be used in large scale(near waste segregation plants) as well as in small scale as this technology improves and can be economically suited 

## Built With⚒️:
**Python as the programing language:** Python is used as the main programming language as it runs smoothly, easy to program, errors can be identified fast due to  its simplicity, and it is a powerful tool 


**Pygame for visualisation**: As I don't have suffecient time or resources to do it physically I used pygame(an open source free python library) to visualize or immitate the physical environment and show how this works. Due to its fast 2D object modeling, easily understandeble visual object moddeling and ease of loading through python made it most desirable for this project. 

## **Layout and Object Modeling📐**

### **Layout:** ### 
Nothing special here just a normal white background with bin at the centre and different waste type slots at the bottom(Solid, Liquid, Hazardous,etc)

![SWTS preview](SWTS1.png)

### **The Bin Mechanism⚙️⚙️:** ###

<ins> **The bin:** </ins>  
The bin has two sliding doors that open upon detecting an entity(for eg, a human or a waste) in its proximity and close when the trash is thrown into the bin in the trash inters into a section where it detects what type of trash it is it.

<ins> **The Scanner:** </ins> <br/>
The scanner is a first real part of this which gives it the name "Smart". The scanner detects what type of trash the thrown is and gives the intput to the computer in the bin which sorts the trash according to its type.

<ins> **The Trash:** </ins> <br/> 
The trash is colour codded according to what type of trash it is

**Solid🟨**-Colour coded as yellow 

**Liquid🟦**-Colour coded as blue

**Organic🟩**-Colour coded as green

**Recyclable🟧**-Colour coded as Orange

**Hazardous🟥**-Colour coded as Red. I put the chances of it appearing in the simulation as 0.0000000000001 as it is very rare for a hazardous item to really come in a public place. 

<ins> **The Visitor:** </ins> <br/>
This is an entity that drops the trash into the bin. Initially while I was making this project I took the entity as a person throwing trash into the bin but later I realized in a real world senrario it will take a long time for this kind of a machine to bring in public places like parks, hotels, etc due its it sheer setup costs and maintance costs so I want a vistor to be of two types one for large scale and small scale. 

**Visitor for Large scale:** Usage of this in large scale means in Factories, Material Recovery Facilities (MRFs) or Waste Sorting Plants, or recycle centres where instead of each individual area all the trash comes to one area and get sorted. Although in the final pygame simulation it dosen't look like it is in large scale, even for large scale implementation in is a very identical process to this. Instead of the visitor being a person we can take it as conveyor belt or robots. Of course there would be more trash and multiple of these will work at the same time. Usage of this in large scale will make waste disposal more envieromentally friendly, saves time, and room for further recycling and innovative waste disposal increases.Ultimately, making waste disposal more efficient.   

**Visitor in small scale:** This was my initial idea of this project. Although, later i realised this is economically not feasible I didn't completly rule out this idea. As the usage of this machines increases, as the technology develops, as smart cities grow the usage of this in public or maybe even private spaces increases. Imagine just having a lot of trash at home but you don't have to worry about where you have to throw it as you have this bin in your house and you can just deposit it there and it will sort on its own. The advantages of this are unlike in large scale where you bring everything to one place and then it gets sorted you have to transport all these sorted trash to the respective areas we can just directly take the sorted trash to their respective areas directly (for eg, Recyclable waste can be directly taken to the recycling plant). This also increases effciency and cuts travel costs. 

## Workflow of the System 🧠🚀

![SWTS preview](SWTS.gif)

