from rdflib import Graph, Literal, RDF, URIRef, Namespace

# Create RDF Graph
g = Graph()

# Namespace
CB = Namespace("http://example.org/cyberbullying#")

# Define classes
User = CB.User
Message = CB.Message
BullyingType = CB.BullyingType

# Define properties
sendsMessage = CB.sendsMessage
hasBullyingType = CB.hasBullyingType
messageText = CB.messageText

# Sample data
user1 = CB.User1
msg1 = CB.Message1

# Input message
text = "You are stupid and useless"

# Bullying keywords
bullying_words = ["stupid", "idiot", "useless", "hate", "kill"]

# Detection logic
is_bullying = any(word in text.lower() for word in bullying_words)

# Add RDF triples
g.add((user1, RDF.type, User))
g.add((msg1, RDF.type, Message))
g.add((user1, sendsMessage, msg1))
g.add((msg1, messageText, Literal(text)))

if is_bullying:
    g.add((msg1, hasBullyingType, CB.VerbalAbuse))
    print("🚨 Cyberbullying Detected")
else:
    print("✅ No Cyberbullying Detected")

# Save RDF file
g.serialize("cyberbullying_data.rdf", format="xml")
