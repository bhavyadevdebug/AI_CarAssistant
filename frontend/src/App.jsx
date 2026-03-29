import LoginForm from "./LoginForm";

function App() {
  return (
    <>
      {/* Navbar */}
      <nav className="bg-blue-600 text-white px-6 py-3 flex justify-between items-center shadow">
        <h1 className="text-xl font-bold">Car Lease Analyzer</h1>
        <div className="space-x-4">
          <a href="#" className="hover:text-gray-200">Home</a>
          <a href="#" className="hover:text-gray-200">Docs</a>
          <a href="#" className="hover:text-gray-200">About</a>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
        <h1 className="text-4xl font-bold text-blue-600 mb-4">Get Started 🚀</h1>
        <LoginForm />
      </section>
    </>
  );
}

export default App;
