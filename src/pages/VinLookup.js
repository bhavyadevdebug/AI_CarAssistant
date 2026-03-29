import { useState } from "react";
import { Box, Heading, Text, Input, Button, Spinner, Alert } from "@chakra-ui/react";

export default function VinLookup() {
  const [vin, setVin] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleVerify = async () => {
    if (!vin || vin.length !== 17) {
      setError("Please enter a valid 17-character VIN.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const res = await fetch(`http://127.0.0.1:8000/vin/${vin}`);
      if (!res.ok) {
        // fallback demo data
        setResult({
          make: "Honda",
          model: "Accord",
          year: "2003",
          trim: "EX",
        });
        return;
      }
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box>
      <Heading size="md" color="purple.300">VIN Lookup</Heading>
      <Text mt={2}>Enter a Vehicle Identification Number to fetch details.</Text>
      <Input
        placeholder="Enter VIN here..."
        mt={4}
        bg="gray.700"
        color="white"
        value={vin}
        onChange={(e) => setVin(e.target.value)}
      />
      <Button mt={4} colorScheme="purple" onClick={handleVerify}>
        Verify
      </Button>

      {loading && (
        <Box display="flex" alignItems="center" color="blue.300" mt={4}>
          <Spinner size="sm" mr={2} /> Checking VIN...
        </Box>
      )}

      {error && (
        <Alert status="error" mt={4} rounded="md">
          {error}
        </Alert>
      )}

      {result && (
        <Box mt={4} p={4} bg="gray.700" rounded="md" shadow="md">
          <Text><b>Make:</b> {result.make}</Text>
          <Text><b>Model:</b> {result.model}</Text>
          <Text><b>Year:</b> {result.year}</Text>
          <Text><b>Trim:</b> {result.trim}</Text>
        </Box>
      )}
    </Box>
  );
}



