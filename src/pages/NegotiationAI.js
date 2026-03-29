import { useState } from "react";
import { Box, Heading, Text, Input, Button } from "@chakra-ui/react";

export default function NegotiationAI() {
  const [terms, setTerms] = useState("");
  const [suggestions, setSuggestions] = useState(null);

  const handleNegotiate = async () => {
    const res = await fetch("http://127.0.0.1:8000/negotiate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ terms }),
    });
    const data = await res.json();
    setSuggestions(data);
  };

  return (
    <Box>
      <Heading size="md" color="purple.300">Negotiation AI</Heading>
      <Text mt={2}>Get AI-powered suggestions to negotiate better terms.</Text>

      <Input
        placeholder="Paste contract terms here..."
        mt={4}
        bg="gray.700"
        color="white"
        value={terms}
        onChange={(e) => setTerms(e.target.value)}
      />
      <Button mt={4} colorScheme="purple" onClick={handleNegotiate}>
        Get Suggestions
      </Button>

      {suggestions && (
        <Box mt={4} p={4} bg="gray.700" rounded="md">
          <Text><b>Suggestions:</b></Text>
          <Text>{suggestions.message}</Text>
        </Box>
      )}
    </Box>
  );
}


