import { useState } from "react";

export default function NegotiationChat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;
    const userMsg = { role: "user", text: input };
    setMessages([...messages, userMsg]);

    // TODO: Replace with backend LLM call
    const botMsg = { role: "bot", text: "This clause can be negotiated by..." };
    setMessages((prev) => [...prev, botMsg]);
    setInput("");
  };

  return (
    <div className="border p-4 rounded">
      <h2 className="text-xl font-bold mb-4">Negotiation Assistant</h2>
      <div className="h-64 overflow-y-auto border p-2 mb-4">
        {messages.map((m, i) => (
          <div key={i} className={m.role === "user" ? "text-right" : "text-left"}>
            <p className={m.role === "user" ? "bg-blue-200 inline-block p-2 rounded" : "bg-gray-200 inline-block p-2 rounded"}>
              {m.text}
            </p>
          </div>
        ))}
      </div>
      <div className="flex">
        <input
          className="flex-grow border p-2 rounded mr-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage} className="bg-orange-500 text-white px-4 py-2 rounded">
          Send
        </button>
      </div>
    </div>
  );
}