VALID_COLLECTION_SAMPLE_DATA = {
    "title": "test title 4",
    "description": "test description 1",
    "movies": [
        {
            "title": "Папа",
            "description": 'Based on A. Galych\'s play "Matrosskaya Tishina", "Papa" tells a story of a Jewish father who dreamed of seeing his son perform on a stage in front of huge audiences, he dreamed of seeing him as the greatest violinist of his time. To achieve the goal he taught his son Dodik how to play the violin from the yearly age. When Dodik grew up he left the small town he and his father lived in to study in the Moscow Conservatory leaving his past behind. But one day he has to choose either to loose his father or everything he has achieved.',
            "genres": "Drama",
            "uuid": "9995aa3a-e7d1-454f-9fb6-f7cfa5cae3c0",
        },
        {
            "title": "Beduin",
            "description": "Rita's daughter is sick with leukemia. In order to obtain the money for a bone marrow transplant, she travels from Ukraine to Russia to become a surrogate mother. The homosexual couple who are the biological parents of the child die in an automobile accident. Rita is left six month pregnant, without any money, and with a dying daughter to care for. In order to save her daughter, Rita is prepared to do anything. She's drawn into the criminal world, from which she escapes with her daughter to Jordan in the Near East, where Bedouins treat cancer by means of nontraditional medicines.",
            "genres": "Drama,Action",
            "uuid": "d2be5eec-9ea0-41f7-8d8f-8d17d1c6a917",
        },
        {
            "title": "Puteshestvie s domashnimi zhivotnymi",
            "description": "Plucked from an orphanage as a literal love slave, the now adult Natalija (a luminous Kseniya Kutepova) serves her ape-like husband by tending his prized cow—whose milk they sell to customers on passing trains. When hubby suddenly drops dead, however, Natalija’s narrow life of cows and rails finally starts opening up. Dumping his body at the local hospital, dropping by church to say a few prayers and trading in the cow for a pet goat, she slowly eliminates all trace of his former hold on her, searching out a new life in the freedom that emerges.",
            "genres": "Romance,Drama",
            "uuid": "c8692919-5ce9-45e9-bfdd-d714234778c2",
        },
        {
            "title": "Корпоратив",
            "description": "Igor, a furniture store manager, tries to figure out what happened during the corporate event which resulted his store to be completely destroyed.",
            "genres": "Comedy",
            "uuid": "331d8e1a-cce0-478b-823d-c4fc34473a20",
        },
        {
            "title": "Чудо",
            "description": 'The film is based on real events that took place in Samara in 1956 and known as the "Standing Zoe." During the holiday girl, without waiting her betrothed, removes the icon from the wall and Nicholas begins to dance with her, but suddenly freezes in place. This state continues for many months. Residents of the provincial town are frightened by this extraordinary event, which is cluttered with rumors and speculation. To try to understand the situation, there goes metropolitan newspaper journalist ...',
            "genres": "Drama,History,Mystery",
            "uuid": "8c439d1f-377e-47b3-8e17-66e6a484e619",
        },
    ],
}


INVALID_TITLE_COLLECTION_SAMPLE_DATA = {
    "title": "",
    "description": "test description 1",
    "movies": [
        {
            "title": "Папа",
            "description": 'Based on A. Galych\'s play "Matrosskaya Tishina", "Papa" tells a story of a Jewish father who dreamed of seeing his son perform on a stage in front of huge audiences, he dreamed of seeing him as the greatest violinist of his time. To achieve the goal he taught his son Dodik how to play the violin from the yearly age. When Dodik grew up he left the small town he and his father lived in to study in the Moscow Conservatory leaving his past behind. But one day he has to choose either to loose his father or everything he has achieved.',
            "genres": "Drama",
            "uuid": "9995aa3a-e7d1-454f-9fb6-f7cfa5cae3c0",
        },
        {
            "title": "Beduin",
            "description": "Rita's daughter is sick with leukemia. In order to obtain the money for a bone marrow transplant, she travels from Ukraine to Russia to become a surrogate mother. The homosexual couple who are the biological parents of the child die in an automobile accident. Rita is left six month pregnant, without any money, and with a dying daughter to care for. In order to save her daughter, Rita is prepared to do anything. She's drawn into the criminal world, from which she escapes with her daughter to Jordan in the Near East, where Bedouins treat cancer by means of nontraditional medicines.",
            "genres": "Drama,Action",
            "uuid": "d2be5eec-9ea0-41f7-8d8f-8d17d1c6a917",
        },
        {
            "title": "Puteshestvie s domashnimi zhivotnymi",
            "description": "Plucked from an orphanage as a literal love slave, the now adult Natalija (a luminous Kseniya Kutepova) serves her ape-like husband by tending his prized cow—whose milk they sell to customers on passing trains. When hubby suddenly drops dead, however, Natalija’s narrow life of cows and rails finally starts opening up. Dumping his body at the local hospital, dropping by church to say a few prayers and trading in the cow for a pet goat, she slowly eliminates all trace of his former hold on her, searching out a new life in the freedom that emerges.",
            "genres": "Romance,Drama",
            "uuid": "c8692919-5ce9-45e9-bfdd-d714234778c2",
        },
        {
            "title": "Корпоратив",
            "description": "Igor, a furniture store manager, tries to figure out what happened during the corporate event which resulted his store to be completely destroyed.",
            "genres": "Comedy",
            "uuid": "331d8e1a-cce0-478b-823d-c4fc34473a20",
        },
        {
            "title": "Чудо",
            "description": 'The film is based on real events that took place in Samara in 1956 and known as the "Standing Zoe." During the holiday girl, without waiting her betrothed, removes the icon from the wall and Nicholas begins to dance with her, but suddenly freezes in place. This state continues for many months. Residents of the provincial town are frightened by this extraordinary event, which is cluttered with rumors and speculation. To try to understand the situation, there goes metropolitan newspaper journalist ...',
            "genres": "Drama,History,Mystery",
            "uuid": "8c439d1f-377e-47b3-8e17-66e6a484e619",
        },
    ],
}


INVALID_DESC_COLLECTION_SAMPLE_DATA = {
    "title": "sample title",
    "description": "",
    "movies": [
        {
            "title": "Папа",
            "description": 'Based on A. Galych\'s play "Matrosskaya Tishina", "Papa" tells a story of a Jewish father who dreamed of seeing his son perform on a stage in front of huge audiences, he dreamed of seeing him as the greatest violinist of his time. To achieve the goal he taught his son Dodik how to play the violin from the yearly age. When Dodik grew up he left the small town he and his father lived in to study in the Moscow Conservatory leaving his past behind. But one day he has to choose either to loose his father or everything he has achieved.',
            "genres": "Drama",
            "uuid": "9995aa3a-e7d1-454f-9fb6-f7cfa5cae3c0",
        },
        {
            "title": "Beduin",
            "description": "Rita's daughter is sick with leukemia. In order to obtain the money for a bone marrow transplant, she travels from Ukraine to Russia to become a surrogate mother. The homosexual couple who are the biological parents of the child die in an automobile accident. Rita is left six month pregnant, without any money, and with a dying daughter to care for. In order to save her daughter, Rita is prepared to do anything. She's drawn into the criminal world, from which she escapes with her daughter to Jordan in the Near East, where Bedouins treat cancer by means of nontraditional medicines.",
            "genres": "Drama,Action",
            "uuid": "d2be5eec-9ea0-41f7-8d8f-8d17d1c6a917",
        },
        {
            "title": "Puteshestvie s domashnimi zhivotnymi",
            "description": "Plucked from an orphanage as a literal love slave, the now adult Natalija (a luminous Kseniya Kutepova) serves her ape-like husband by tending his prized cow—whose milk they sell to customers on passing trains. When hubby suddenly drops dead, however, Natalija’s narrow life of cows and rails finally starts opening up. Dumping his body at the local hospital, dropping by church to say a few prayers and trading in the cow for a pet goat, she slowly eliminates all trace of his former hold on her, searching out a new life in the freedom that emerges.",
            "genres": "Romance,Drama",
            "uuid": "c8692919-5ce9-45e9-bfdd-d714234778c2",
        },
        {
            "title": "Корпоратив",
            "description": "Igor, a furniture store manager, tries to figure out what happened during the corporate event which resulted his store to be completely destroyed.",
            "genres": "Comedy",
            "uuid": "331d8e1a-cce0-478b-823d-c4fc34473a20",
        },
        {
            "title": "Чудо",
            "description": 'The film is based on real events that took place in Samara in 1956 and known as the "Standing Zoe." During the holiday girl, without waiting her betrothed, removes the icon from the wall and Nicholas begins to dance with her, but suddenly freezes in place. This state continues for many months. Residents of the provincial town are frightened by this extraordinary event, which is cluttered with rumors and speculation. To try to understand the situation, there goes metropolitan newspaper journalist ...',
            "genres": "Drama,History,Mystery",
            "uuid": "8c439d1f-377e-47b3-8e17-66e6a484e619",
        },
    ],
}


UPDATED_COLLECTION_SAMPLE_DATA = {
    "title": "test title updated",
    "description": "test description updated",
    "movies": [
        {
            "title": "Папа",
            "description": 'Based on A. Galych\'s play "Matrosskaya Tishina", "Papa" tells a story of a Jewish father who dreamed of seeing his son perform on a stage in front of huge audiences, he dreamed of seeing him as the greatest violinist of his time. To achieve the goal he taught his son Dodik how to play the violin from the yearly age. When Dodik grew up he left the small town he and his father lived in to study in the Moscow Conservatory leaving his past behind. But one day he has to choose either to loose his father or everything he has achieved.',
            "genres": "Drama",
            "uuid": "9995aa3a-e7d1-454f-9fb6-f7cfa5cae3c0",
        },
        {
            "title": "Beduin",
            "description": "Rita's daughter is sick with leukemia. In order to obtain the money for a bone marrow transplant, she travels from Ukraine to Russia to become a surrogate mother. The homosexual couple who are the biological parents of the child die in an automobile accident. Rita is left six month pregnant, without any money, and with a dying daughter to care for. In order to save her daughter, Rita is prepared to do anything. She's drawn into the criminal world, from which she escapes with her daughter to Jordan in the Near East, where Bedouins treat cancer by means of nontraditional medicines.",
            "genres": "Drama,Action",
            "uuid": "d2be5eec-9ea0-41f7-8d8f-8d17d1c6a917",
        },
        {
            "title": "Puteshestvie s domashnimi zhivotnymi",
            "description": "Plucked from an orphanage as a literal love slave, the now adult Natalija (a luminous Kseniya Kutepova) serves her ape-like husband by tending his prized cow—whose milk they sell to customers on passing trains. When hubby suddenly drops dead, however, Natalija’s narrow life of cows and rails finally starts opening up. Dumping his body at the local hospital, dropping by church to say a few prayers and trading in the cow for a pet goat, she slowly eliminates all trace of his former hold on her, searching out a new life in the freedom that emerges.",
            "genres": "Romance,Drama",
            "uuid": "c8692919-5ce9-45e9-bfdd-d714234778c2",
        },
    ],
}

UPDATED_EMPTY_MOVIES_SAMPLE_DATA = {
    "movies": [],
}

UPDATED_TITLE_MOVIES_SAMPLE_DATA = {"title": "This title is updated"}


UPDATED_DESC_MOVIES_SAMPLE_DATA = {"description": "This description is updated"}
