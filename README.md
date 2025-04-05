# Projet d'Électronique : Débruitage de Vuvuzela

## Introduction

Ce projet a pour objectif de réduire le bruit des vuvuzelas dans les enregistrements audio, un problème notable lors de la Coupe du Monde de football 2010. Les vuvuzelas produisent des sons monotones et puissants à des fréquences spécifiques, perturbant les retransmissions audio des matchs. Ce projet explore des solutions basées sur des filtres analogiques pour isoler et atténuer ces fréquences indésirables tout en préservant la qualité des commentaires sportifs.

## Objectifs

- Identifier les fréquences caractéristiques des vuvuzelas grâce à une analyse spectrale.
- Étudier et concevoir des filtres réjecteurs capables d'éliminer ces fréquences spécifiques.
- Comparer les performances des filtres conçus, à la fois en simulation et en laboratoire.

## Méthodologie

### Analyse Spectrale du Signal

L'analyse spectrale du signal sonore a permis d'identifier les composantes fréquentielles des vuvuzelas. Les fréquences principales identifiées sont :

- $f_{01} = 235 \text{Hz}$
- $f_{02} = 710 \text{Hz}$
- $f_{03} = 1181 \text{Hz}$
- $f_{04} = 1402 \text{Hz}$

### Étude et Comparaison des Filtres Réjecteurs

Trois types de filtres réjecteurs ont été étudiés :

1. **Filtre RLC** : Non adapté en raison des valeurs de résistances trop basses pour une précision suffisante.
2. **Filtre Twin T passif** : Non adapté en raison de sa bande trop large, perturbant le signal audio.
3. **Filtre Twin T actif** : Adapté grâce à ses valeurs précises et sa performance validée par simulation.

### Mise en Cascade

Le filtre Twin T actif a été retenu et mis en cascade pour traiter les quatre fréquences identifiées. Les simulations et les tests en laboratoire ont confirmé l'efficacité de cette approche.

## Résultats

Les résultats obtenus montrent une bonne concordance entre les calculs théoriques, les simulations et les mesures expérimentales. Les filtres conçus permettent d'atténuer efficacement les fréquences des vuvuzelas tout en préservant la qualité des commentaires audio.

## Contenu du Répertoire

- **Rapport** : Document PDF détaillant le projet, la méthodologie et les résultats.
- **Fichiers Python** : Scripts utilisés pour l'analyse spectrale et le calcul des composants des filtres.
- **Fichiers LTspice** : Simulations des filtres conçus pour valider leur performance.

## Installation et Utilisation

1. Clonez ce dépôt :
```bash
git clone https://github.com/jankolps/projet-vuvuzela.git
```

3. Allez dans le dossier contenant les programmes :
```bash
cd projet-vuvuzela/src
```

3. Installer les dépendances:
```bash
pip install -r requirements.txt
```

## Contributeurs

Kenji Sevik\
Jean Lepers
