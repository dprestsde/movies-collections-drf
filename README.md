# Setup

#### Clone the project by 
` git clone https://github.com/dprestsde/movie-collection-apis.git`

#### steps to setup 
- Create a virtual environment and activate it.
- Navigate to the project's root directory
- Install all required packages by running 
  `pip install -r requirements.txt`

**Please make sure the setting has Movies APis keys i.e., username and password**

#### Run unit tests
Unit tests can be run by the below command 
` python manage.py test `

#### API's documentation

title: Used to register a new user   
URL: `http://localhost:8000/auth/register/`   
method: POST    
request body: { 
       "username": "testusername",
       "password": "testpassword@credy"
       }   
response: {
    "access_token": "59f19b1ae828b54b28dd210c4af3c715b3102c70"
}   

title: Used to retrieve the token to pass authorization for further requests    
URL: http://localhost:8000/auth/register/    
method: POST     
request body:    
    {   
       "username": "testusername",    
       "password": "testpassword@credy"    
       }       
response: {    
    "access_token": "59f19b1ae828b54b28dd210c4af3c715b3102c70"    
}      

title: used to retrieve movies list      
url: http://localhost:8000/movies/list/?page=2     
method: GET      
request body: none     
response: {        
    "count": 45466,    
    "next": "https://demo.credy.in/api/v1/maya/movies/?page=3",       
    "previous": "https://demo.credy.in/api/v1/maya/movies/",       
    "results": [       
        {         
            "title": "San Michele aveva un gallo",      
            "description": "Sentenced to life imprisonment for illegal activities, Italian International member Giulio Manieri holds on to his political ideals while struggling against madness in the loneliness of his prison cell.",       
            "genres": "",       
            "uuid": "cc51020f-1bd6-42ad-84e7-e5c0396435a8"       
        },        
        {        
            "title": "The Morning After",         
            "description": "The Morning After is a feature film that consists of 8 vignettes that are inter-cut throughout the film. The 8 vignettes are about when you wake up next to someone the next morning...",         
            "genres": "Comedy,Drama",         
            "uuid": "9a4fcb67-24f6-4cda-8f49-ad66b689f481"        
        },        
        {           
            "title": "Maa",       
            "description": "The bliss of a biology teacher’s family life in Delhi is shattered when her daughter, Arya  is physically assaulted by Jagan and gang. Does Devki Sabarwal wait for the law to take its course? Or does Devki become Maa Durga and hunt down the perpetrators of the crime?",        
            "genres": "Crime,Drama,Thriller",         
            "uuid": "587a1f5b-d36a-41a3-8bf8-ea0788ebc752"       
        },         
        {         
            "title": "Deep Hearts",       
            "description": "Deep Hearts is a film about the Bororo Fulani, a nomadic society located in central Niger Republic and the title is a reference to an important aspect of these people’s thought and demeanor.",        
            "genres": "Documentary",     
            "uuid": "39409bc2-85e7-4a2c-a236-956dda88cfda"      
        },       
        {         
            "title": "Nouvelles luttes extravagantes",      
            "description": "A series of fantastical wrestling matches.",        
            "genres": "Comedy,Fantasy",        
            "uuid": "befbf9f7-0ec0-48ad-b77c-2ba2a84bfe5c"       
        },       
        {        
            "title": "L'Homme orchestre",     
            "description": "A band-leader has arranged seven chairs for the members of his band. When he sits down in the first chair, a cymbal player appears in the same chair, then rises and sits in the next chair. As the cymbal player sits down, a drummer appears in the second chair, and then likewise moves on to the third chair. In this way, an entire band is soon formed, and is then ready to perform.",      
            "genres": "Fantasy,Action,Thriller",          
            "uuid": "cc75c16e-c72d-444f-93db-1b8764555be0"        
        },       
        {       
            "title": "Pooh's Heffalump Halloween Movie",              
            "description": "It's Halloween in the 100 Acre Wood, and Roo's best new friend, Lumpy, is looking forward to his first time trick-or-treating. That is, until Tigger warns them about the scary Gobloon, who'll turn them into jack-o'-lanterns if he catches them. But if Roo and Lumpy turn the tables on the Gobloon, they get to make a wish! Lumpy and Roo decide to be \"brave together, brave forever\" and catch the Gobloon so they can make their wishes come true.",         
            "genres": "Animation,Family",     
            "uuid": "d2c99a80-1360-4872-8735-d8d1461e0e8f"        
        },            
        {        
            "title": "Les Transmutations imperceptibles",          
            "description": "This shows a prince entering upon the stage of the King's private theatre. He is about to do a few mystifying tricks for the amusement of the court.",               
            "genres": "",         
            "uuid": "13ecfdcc-1680-44d8-a9e7-a0d4c6e9386a"           
        },      
        {            
            "title": "Le Roi du maquillage",          
            "description": "The background of this picture represents a scene along the beautiful river Seine in Paris. A gentleman enters, and taking a blackboard from the side of the picture, he draws on it a sketch of a novelist. Then, standing in the centre, he causes the living features of his sketch to appear in the place of his own, which is utterly devoid of whiskers. The change is made so mysteriously that the eye cannot notice it until one sees quite another person in the place of the first. Again another sketch is shown on the board, this one being that of a miser; then an English cockney; a comic character; a French policeman, and last of all, the grinning visage of Mephistopheles. It is almost impossible to give this film a more definite description; suffice it to say that it is something entirely new in motion pictures and is sure to please. Written by Méliès Catalog",          
            "genres": "",          
            "uuid": "dd74504d-dc41-4c75-9fc3-3518ded48ff8"          
        },          
        {          
            "title": "Le locataire diabolique",          
            "description": "A man rents an apartment and furnishes it in remarkable fashion.",          
            "genres": "Fantasy,Comedy",          
            "uuid": "3d9f7f3f-08bf-4200-b66f-d29976683a5f"          
        }          
    ]          
}          


title: use retrieve collection data      
url: http://localhost:8000/movies/collection/     
body: none       
method: get      
response: {      
    "is_success": true,    
    "collection": [          
        {          
            "title": "test title 4",          
            "description": "test description 1",          
            "uuid": "f1753720-bd83-42e8-8217-2253cdcdca3b"          
        },          
        {          
            "title": "test title 4",          
            "description": "test description 1",          
            "uuid": "a313e35a-9a99-4c13-a0d2-a0c797dc58b6"          
        },          
        {          
            "title": "test title 4",          
            "description": "test description 1",          
            "uuid": "22a105dc-9dc9-41d6-8552-b6cfe82ed4f9"          
        },          
        {          
            "title": "test title 4",          
            "description": "test description 1",          
            "uuid": "21f09163-1358-4d03-9433-073886e98c36"          
        },          
        {          
            "title": "test title 4",          
            "description": "test description 1",          
            "uuid": "91020c70-0646-4898-a59e-6ada6aa5bb12"          
        },          
        {          
            "title": "test title 4",          
            "description": "test description 1",          
            "uuid": "c732f260-b14c-4308-ad77-cd76872fb2e6"          
        },          
        {          
            "title": "test title 5",          
            "description": "test description 1",          
            "uuid": "bbf5b3db-caac-406e-97fb-9702814db3a3"          
        }          
    ],          
    "favourite_genres": "Drama, Comedy, History"          
}          
}          


title: use to create a collection and associated data          
url: http://localhost:8000/movies/collection/          
method: post          
request body: {          
    "title": "test ", 
    "description": "test description 1", 
    "movies": [
        {
            "title": "Папа",
            "description": "Based on A. Galych's play \"Matrosskaya Tishina\", \"Papa\" tells a story of a Jewish father who dreamed of seeing his son perform on a stage in front of huge audiences, he dreamed of seeing him as the greatest violinist of his time. To achieve the goal he taught his son Dodik how to play the violin from the yearly age. When Dodik grew up he left the small town he and his father lived in to study in the Moscow Conservatory leaving his past behind. But one day he has to choose either to loose his father or everything he has achieved.",
            "genres": "Drama",
            "uuid": "9995aa3a-e7d1-454f-9fb6-f7cfa5cae3c0"
        },
        {
            "title": "Beduin",
            "description": "Rita's daughter is sick with leukemia. In order to obtain the money for a bone marrow transplant, she travels from Ukraine to Russia to become a surrogate mother. The homosexual couple who are the biological parents of the child die in an automobile accident. Rita is left six month pregnant, without any money, and with a dying daughter to care for. In order to save her daughter, Rita is prepared to do anything. She's drawn into the criminal world, from which she escapes with her daughter to Jordan in the Near East, where Bedouins treat cancer by means of nontraditional medicines.",
            "genres": "Drama,Action",
            "uuid": "d2be5eec-9ea0-41f7-8d8f-8d17d1c6a917"
        },
        {
            "title": "Puteshestvie s domashnimi zhivotnymi",
            "description": "Plucked from an orphanage as a literal love slave, the now adult Natalija (a luminous Kseniya Kutepova) serves her ape-like husband by tending his prized cow—whose milk they sell to customers on passing trains. When hubby suddenly drops dead, however, Natalija’s narrow life of cows and rails finally starts opening up. Dumping his body at the local hospital, dropping by church to say a few prayers and trading in the cow for a pet goat, she slowly eliminates all trace of his former hold on her, searching out a new life in the freedom that emerges.",
            "genres": "Romance,Drama",
            "uuid": "c8692919-5ce9-45e9-bfdd-d714234778c2"
        },
        {
            "title": "Корпоратив",
            "description": "Igor, a furniture store manager, tries to figure out what happened during the corporate event which resulted his store to be completely destroyed.",
            "genres": "Comedy",
            "uuid": "331d8e1a-cce0-478b-823d-c4fc34473a20"
        },
        {
            "title": "Чудо",
            "description": "The film is based on real events that took place in Samara in 1956 and known as the \"Standing Zoe.\" During the holiday girl, without waiting her betrothed, removes the icon from the wall and Nicholas begins to dance with her, but suddenly freezes in place. This state continues for many months. Residents of the provincial town are frightened by this extraordinary event, which is cluttered with rumors and speculation. To try to understand the situation, there goes metropolitan newspaper journalist ...",
            "genres": "Drama,History,Mystery",
            "uuid": "8c439d1f-377e-47b3-8e17-66e6a484e619"
        }]
}

response: {
    "collection_uuid": "bbf5b3db-caac-406e-97fb-9702814db3a3"
}


title: use to return a particular collection details          
url: http://localhost:8000/movies/collection/<uuid>/          
method: get          
request body: none          
response body: {
    "title": "test title 5",
    "description": "test description 1",
    "movies": [
        {
            "uuid": "331d8e1a-cce0-478b-823d-c4fc34473a20",
            "title": "Корпоратив",
            "description": "Igor, a furniture store manager, tries to figure out what happened during the corporate event which resulted his store to be completely destroyed.",
            "genres": "Comedy"
        },
        {
            "uuid": "8c439d1f-377e-47b3-8e17-66e6a484e619",
            "title": "Чудо",
            "description": "The film is based on real events that took place in Samara in 1956 and known as the \"Standing Zoe.\" During the holiday girl, without waiting her betrothed, removes the icon from the wall and Nicholas begins to dance with her, but suddenly freezes in place. This state continues for many months. Residents of the provincial town are frightened by this extraordinary event, which is cluttered with rumors and speculation. To try to understand the situation, there goes metropolitan newspaper journalist ...",
            "genres": "Drama,History,Mystery"
        },
        {
            "uuid": "9995aa3a-e7d1-454f-9fb6-f7cfa5cae3c0",
            "title": "Папа",
            "description": "Based on A. Galych's play \"Matrosskaya Tishina\", \"Papa\" tells a story of a Jewish father who dreamed of seeing his son perform on a stage in front of huge audiences, he dreamed of seeing him as the greatest violinist of his time. To achieve the goal he taught his son Dodik how to play the violin from the yearly age. When Dodik grew up he left the small town he and his father lived in to study in the Moscow Conservatory leaving his past behind. But one day he has to choose either to loose his father or everything he has achieved.",
            "genres": "Drama"
        },
        {
            "uuid": "c8692919-5ce9-45e9-bfdd-d714234778c2",
            "title": "Puteshestvie s domashnimi zhivotnymi",
            "description": "Plucked from an orphanage as a literal love slave, the now adult Natalija (a luminous Kseniya Kutepova) serves her ape-like husband by tending his prized cow—whose milk they sell to customers on passing trains. When hubby suddenly drops dead, however, Natalija’s narrow life of cows and rails finally starts opening up. Dumping his body at the local hospital, dropping by church to say a few prayers and trading in the cow for a pet goat, she slowly eliminates all trace of his former hold on her, searching out a new life in the freedom that emerges.",
            "genres": "Romance,Drama"
        },
        {
            "uuid": "d2be5eec-9ea0-41f7-8d8f-8d17d1c6a917",
            "title": "Beduin1",
            "description": "Rita's daughter is sick with leukemia. In order to obtain the money for a bone marrow transplant, she travels from Ukraine to Russia to become a surrogate mother. The homosexual couple who are the biological parents of the child die in an automobile accident. Rita is left six month pregnant, without any money, and with a dying daughter to care for. In order to save her daughter, Rita is prepared to do anything. She's drawn into the criminal world, from which she escapes with her daughter to Jordan in the Near East, where Bedouins treat cancer by means of nontraditional medicines.",
            "genres": "Drama,Action"
        }
    ]
}

title: use to update a particular collection object          
url: http://localhost:8000/movies/collection/<uuid>/          
method: put          
request body: {          
   
    "movies": [
        {
            "title": "Папа",
            "description": "Based on A. Galych's play \"Matrosskaya Tishina\", \"Papa\" tells a story of a Jewish father who dreamed of seeing his son perform on a stage in front of huge audiences, he dreamed of seeing him as the greatest violinist of his time. To achieve the goal he taught his son Dodik how to play the violin from the yearly age. When Dodik grew up he left the small town he and his father lived in to study in the Moscow Conservatory leaving his past behind. But one day he has to choose either to loose his father or everything he has achieved.",
            "genres": "Drama",
            "uuid": "9995aa3a-e7d1-454f-9fb6-f7cfa5cae3c0"
        },
        {
            "title": "Beduin1",
            "description": "Rita's daughter is sick with leukemia. In order to obtain the money for a bone marrow transplant, she travels from Ukraine to Russia to become a surrogate mother. The homosexual couple who are the biological parents of the child die in an automobile accident. Rita is left six month pregnant, without any money, and with a dying daughter to care for. In order to save her daughter, Rita is prepared to do anything. She's drawn into the criminal world, from which she escapes with her daughter to Jordan in the Near East, where Bedouins treat cancer by means of nontraditional medicines.",
            "genres": "Drama,Action",
            "uuid": "d2be5eec-9ea0-41f7-8d8f-8d17d1c6a917"
        },
        {
            "title": "Puteshestvie s domashnimi zhivotnymi",
            "description": "Plucked from an orphanage as a literal love slave, the now adult Natalija (a luminous Kseniya Kutepova) serves her ape-like husband by tending his prized cow—whose milk they sell to customers on passing trains. When hubby suddenly drops dead, however, Natalija’s narrow life of cows and rails finally starts opening up. Dumping his body at the local hospital, dropping by church to say a few prayers and trading in the cow for a pet goat, she slowly eliminates all trace of his former hold on her, searching out a new life in the freedom that emerges.",
            "genres": "Romance,Drama",
            "uuid": "c8692919-5ce9-45e9-bfdd-d714234778c2"
        },
        {
            "title": "Корпоратив",
            "description": "Igor, a furniture store manager, tries to figure out what happened during the corporate event which resulted his store to be completely destroyed.",
            "genres": "Comedy",
            "uuid": "331d8e1a-cce0-478b-823d-c4fc34473a20"
        },
        {
            "title": "Чудо",
            "description": "The film is based on real events that took place in Samara in 1956 and known as the \"Standing Zoe.\" During the holiday girl, without waiting her betrothed, removes the icon from the wall and Nicholas begins to dance with her, but suddenly freezes in place. This state continues for many months. Residents of the provincial town are frightened by this extraordinary event, which is cluttered with rumors and speculation. To try to understand the situation, there goes metropolitan newspaper journalist ...",
            "genres": "Drama,History,Mystery",
            "uuid": "8c439d1f-377e-47b3-8e17-66e6a484e619"
        }]
}
response body: {
    "title": "test title 5",
    "description": "test description 1",
    "uuid": "bbf5b3db-caac-406e-97fb-9702814db3a3"
}

title: used to delete a particular collection object          
url: http://localhost:8000/movies/collection/<uuid>/          
method: delete          
request body: none          
response body: none          

title: use to retrieve the number of requests the site has received          
url: http://localhost:8000/auth/request-count/          
method: get          
request body: none          
response body: {          
    "count": 27          
}          

title: use to reset visitor count to zero          
url: http://localhost:8000/auth/request-count/reset/          
method: post          
request body: none          
response body: {          
    "message": "request count reset successfully"          
}          




