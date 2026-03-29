import { useState } from "react";
import Upload from "./pages/Upload";
import FairnessReport from "./pages/FairnessReport";
import VinLookup from "./pages/VinLookup";
import NegotiationAI from "./pages/NegotiationAI";
import Login from "./pages/Login";
import { Box, Heading, Stack, Button } from "@chakra-ui/react";

function Sidebar({ page, setPage }) {
  return (
    <Box w="64" bg="gray.900" color="white" p={6}>
      <Heading size="lg" mb={6} color="purple.400">
        LeaseWise AI
      </Heading>
      <Stack spacing={3}>
        <Button
          variant={page === "Upload" ? "solid" : "ghost"}
          colorScheme="purple"
          onClick={() => setPage("Upload")}
        >
          Analyze Contract
        </Button>
        <Button
          variant={page === "Fairness" ? "solid" : "ghost"}
          colorScheme="purple"
          onClick={() => setPage("Fairness")}
        >
          Fairness Report
        </Button>
        <Button
          variant={page === "VIN" ? "solid" : "ghost"}
          colorScheme="purple"
          onClick={() => setPage("VIN")}
        >
          VIN Lookup
        </Button>
        <Button
          variant={page === "Negotiation" ? "solid" : "ghost"}
          colorScheme="purple"
          onClick={() => setPage("Negotiation")}
        >
          Negotiation AI
        </Button>
      </Stack>

      <Box mt={10} p={4} bg="gray.700" rounded="md" fontSize="sm">
        <b>Expert Tip:</b> Scan for “Disposition Fees” — they often hide at the very end of agreements.
      </Box>
    </Box>
  );
}

export default function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [page, setPage] = useState("Upload");

  // Show login screen with dark background until signed in
  if (!loggedIn) {
    return (
      <Box
        minH="100vh"
        bg="gray.900"
        display="flex"
        alignItems="center"
        justifyContent="center"
      >
        <Login onLogin={() => setLoggedIn(true)} />
      </Box>
    );
  }

  // Dashboard layout
  return (
    <Box display="flex" minH="100vh" bg="gray.900" color="gray.100">
      <Sidebar page={page} setPage={setPage} />
      <Box flex="1" p={8}>
        <Box bg="gray.800" shadow="md" rounded="md" p={6}>
          {page === "Upload" && <Upload />}
          {page === "Fairness" && <FairnessReport />}
          {page === "VIN" && <VinLookup />}
          {page === "Negotiation" && <NegotiationAI />}
        </Box>
      </Box>
    </Box>
  );
}
