import sys
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

def get_sentiment(input_text):
    blob = tb(input_text)
    polarity, subjectivity = blob.sentiment
    polarity_perc = f"{100*abs(polarity):.0f}"
    subjectivity_perc = f"{100*subjectivity:.0f}"
    if polarity > 0:
        polarity_str = f"{polarity_perc}% positive"
    elif polarity < 0:
        polarity_str = f"{polarity_perc}% negative"
    else:
        polarity_str = "neutral"
    if subjectivity > 0:
        subjectivity_str = f"{subjectivity}% subjective"
    else:
        subjectivity_str = "perfectly objective"
    print(f"This text is {polarity_str} and {subjectivity_str}.")

print("Dans une réunion, tenue par les socialistes gantois, sous la présidence deM.Anseele, et au cours de laquelle celui-ci a rendu compte de l’assemblée du conseil général du Parti ouvrier, on a discuté de nouveau les moyens de propagande pour l'obtention du S. U. <M. Lamarcq a protesté contre les discours de ceux qui parlent encore de Révolution.")
get_sentiment("Dans une réunion, tenue par les socialistes gantois, sous la présidence deM.Anseele, et au cours de laquelle celui-ci a rendu compte de l’assemblée du conseil général du Parti ouvrier, on a discuté de nouveau les moyens de propagande pour l'obtention du S. U. <M. Lamarcq a protesté contre les discours de ceux qui parlent encore de Révolution.")

print("Il n’est pas nécessaire de répéter que si l’on vous fait assez facilement entrer dans une maison de fous, il est très difficile, si «pas impossible, d’en sortir.")
get_sentiment("Il n’est pas nécessaire de répéter que si l’on vous fait assez facilement entrer dans une maison de fous, il est très difficile,, si «pas impossible, d’en sortir.")

print("A la suite des réclamations des habitants du quartier de la caserne Prince Albert, le colonel baron de Ilcusch vient d’ordonner la suppression des sonneries g'hiôrales.")
get_sentiment("A la suite des réclamations des habitants du quartier de la caserne Prince Albert, le colonel baron de Ilcusch vient d’ordonner la suppression des sonneries g'hiôrales.")

print("Elle est devenue coquette et avide pour Yvette; elle est devenue criminelle pour Yvette encore.")
get_sentiment("Elle est devenue coquette et avide pour Yvette; elle est devenue criminelle pour Yvette encore.")

print("De quelle manière la diplomatie s'attaquera-t-elle à une association qui, avec une telle audace, s'élève au-dessus des conditions générales des rapports de peuple à peuple ?")
get_sentiment("De quelle manière la diplomatie s'attaquera-t-elle à une association qui, avec une telle audace, s'élève au-dessus des conditions générales des rapports de peuple à peuple ?")

print("Il faut donc verser pendant trois ans, un minimum do 3 francs et au total 18 francs, pour avoir droit à la pension.")
get_sentiment("Il faut donc verser pendant trois ans, un minimum do 3 francs et au total 18 francs, pour avoir droit à la pension.")

print("La grande Brasserie de Pilsen « Urquell » informe les consommateurs que ses bières ne se débitent que dans les établissements suivants")
get_sentiment("La grande Brasserie de Pilsen « Urquell » informe les consommateurs que ses bières ne se débitent que dans les établissements suivants")

print("C’est là-dessus qu’allait s’engager hier le procès en succession, lorsqu'un coup de théâtre s’est produit.")
get_sentiment("C’est là-dessus qu’allait s’engager hier le procès en succession, lorsqu'un coup de théâtre s’est produit.")

print("Sa lune de miel vient d’être brusquement troublée.")
get_sentiment("Sa lune de miel vient d’être brusquement troublée.")

print("C’est un singulier mariage, qui vient d’être célébré dans la paroisse d’un des faubourgs de Vienne, à Hietzlng.")
get_sentiment("C’est un singulier mariage, qui vient d’être célébré dans la paroisse d’un des faubourgs de Vienne, à Hietzlng.")
