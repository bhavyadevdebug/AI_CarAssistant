import { Box, Heading, Text, Progress } from "@chakra-ui/react";

export default function FairnessReport() {
  return (
    <Box>
      <Heading size="md" color="purple.300">Fairness Report</Heading>
      <Text mt={2}>Your contract fairness score:</Text>
      <Progress value={65} colorScheme="purple" size="lg" mt={4} rounded="md" />
      <Text mt={2}>Score: 65/100</Text>
    </Box>
  );
}

