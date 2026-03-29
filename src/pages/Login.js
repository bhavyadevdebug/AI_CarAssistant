import { Box, Heading, Text, Input, Button } from "@chakra-ui/react";

export default function Login({ onLogin }) {
  return (
    <Box bg="gray.800" shadow="md" rounded="md" p={6} maxW="sm" mx="auto" mt={20} color="gray.100">
      <Heading size="lg" mb={6} textAlign="center" color="purple.300">LeaseWise AI</Heading>
      <Text mb={6} textAlign="center" color="gray.400">Secure your next car deal with AI</Text>
      <Input type="email" placeholder="Email Address" mb={4} bg="gray.700" border="none" color="white" _placeholder={{ color: "gray.400" }} />
      <Input type="password" placeholder="Password" mb={6} bg="gray.700" border="none" color="white" _placeholder={{ color: "gray.400" }} />
      <Button colorScheme="purple" w="full" onClick={onLogin}>Sign In</Button>
      <Text fontSize="sm" textAlign="center" mt={4} color="gray.400">
        Don’t have an account? <Text as="span" color="blue.400" cursor="pointer">Request Access</Text>
      </Text>
    </Box>
  );
}
