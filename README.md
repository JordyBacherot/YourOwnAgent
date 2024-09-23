# YourOwnAgent

Your Own Agent 🤖 (YOA) est une application visant à l'utilisation d'agent intelligent vous assistant au quotidien.

Ces Agents reposent sur des Inteligences Artificielles de type textuel

Ces agents sont liée à des outils de planification de tâches et d'emploie du temps, permettant ainsi de faciliter votre quotidien. Le tout dans une démarche cognitive pour conserver un aspect ludique tout en maximisant votre efficacité.

## Pour commencer

Cette application est customisable sur de nombreux points.

Elle contient d'abord une partie avec vos agents IA, qui seront utilisables via des clés d'API ChatGpt ou Groq mais aussi directement sur votre ordinateur grâce à Ollama (si des agent IA fonctionnant localement sur votre PC vous intéresse je vous invite à vous diriger vers la partie Installation avec Ollama)

Puis une seconde partie sur de la gestion de tâche et d'emploi du temps directement liée à vos Agents.

## Installation


### Dépendances 

Grâce à la librairie Poetry
Installer poetry :

```bash
pip install poetry
```

Installer les dépendances :

```bash
poetry install
```

ou avec les requirements.txt

```bash
pip install -r requirements.txt
```

## Lancement de l'application 

```bash
streamlit run GUI/Launcher.py
```

## Sous fonctionalités

### Exporter les dépendances 

Avec poetry :

```bash
poetry export -f requirements.txt --output requirements.txt
```

### Ollama

Afin de pouvoir exploiter l'entièreté de l'application, il est conseillé de télécharger Ollama, qui vous permettra d'utiliser vos agents IA localement sur votre ordinateur

⚠️ Cette méthode consommera des ressources sur votre ordinateur !

## Librairies Principales Utilisées

### Langchain
Librairie facilitant l'implémentation des LLM et des outils

### Streamlit 
Interface Graphique

## Auteur

Jordy Bacherot