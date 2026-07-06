import { useState } from "react";
import axios from "axios";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) setSelectedFile(file);
  };

  const sendMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message,
      });

      setResponse(res.data.response);
    } catch {
      setResponse("Unable to connect to the backend.");
    }

    setLoading(false);
  };

  const uploadPDF = async () => {
    if (!selectedFile) {
      alert("Please select a PDF first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      alert(res.data.message);
    } catch {
      alert("Upload failed.");
    }

    setLoading(false);
  };

  const getSummary = async () => {
    setLoading(true);

    try {
      const res = await axios.get("http://127.0.0.1:8000/summary");
      setResponse(res.data.summary);
    } catch {
      setResponse("Unable to generate summary.");
    }

    setLoading(false);
  };

  const getQuiz = async () => {
    setLoading(true);

    try {
      const res = await axios.get("http://127.0.0.1:8000/quiz");
      setResponse(res.data.quiz);
    } catch {
      setResponse("Unable to generate quiz.");
    }

    setLoading(false);
  };

  const getPlanner = async () => {
    setLoading(true);

    try {
      const res = await axios.get("http://127.0.0.1:8000/planner");
      setResponse(res.data.planner);
    } catch {
      setResponse("Unable to generate study plan.");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 via-slate-100 to-indigo-100">

      <header className="bg-blue-700 text-white shadow-lg">
        <div className="max-w-6xl mx-auto p-6">
          <h1 className="text-4xl font-bold">
            📚 StudyBuddy AI
          </h1>
          <p className="text-blue-100 mt-2">
            AI-powered learning assistant for students
          </p>
        </div>
      </header>

      <main className="max-w-6xl mx-auto p-8">

        <div className="grid grid-cols-2 md:grid-cols-4 gap-5 mb-8">

          <label className="bg-white rounded-2xl shadow-lg p-6 text-center cursor-pointer hover:scale-105 transition">
            📄
            <h2 className="font-bold mt-3">Upload PDF</h2>

            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
              className="hidden"
            />
          </label>

          <button
            onClick={getSummary}
            className="bg-white rounded-2xl shadow-lg p-6 hover:scale-105 transition"
          >
            📝
            <h2 className="font-bold mt-3">Summary</h2>
          </button>

          <button
            onClick={getQuiz}
            className="bg-white rounded-2xl shadow-lg p-6 hover:scale-105 transition"
          >
            ❓
            <h2 className="font-bold mt-3">Quiz</h2>
          </button>

          <button
            onClick={getPlanner}
            className="bg-white rounded-2xl shadow-lg p-6 hover:scale-105 transition"
          >
            📅
            <h2 className="font-bold mt-3">Study Planner</h2>
          </button>

        </div>

        {selectedFile && (
          <div className="bg-green-100 border border-green-400 rounded-xl p-4 mb-5 flex justify-between items-center">

            <span>
              ✅ <strong>{selectedFile.name}</strong>
            </span>

            <button
              onClick={uploadPDF}
              className="bg-green-600 hover:bg-green-700 text-white px-5 py-2 rounded-lg"
            >
              Upload
            </button>

          </div>
        )}

        <div className="bg-white rounded-2xl shadow-xl">

          <div className="border-b p-5">
            <h2 className="text-xl font-bold">
            🦉Buddy's response
            </h2>
          </div>

          <div className="h-[500px] overflow-y-auto p-6">

            {!response && !loading && (
              <div className="text-gray-500">
                Upload a PDF, then generate a Summary, Quiz, Study Plan, or chat with StudyBuddy AI.
              </div>
            )}

            {loading && (
              <div className="text-blue-700 text-lg font-semibold animate-pulse">
                🦉 Generating response...
              </div>
            )}

            {!loading && response && (
              <div className="bg-blue-50 rounded-xl p-5 whitespace-pre-wrap leading-8">
                {response}
              </div>
            )}

          </div>

          <div className="border-t p-5 flex gap-3">

            <input
              className="flex-1 border rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Ask anything about your study materials..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
            />

            <button
              onClick={sendMessage}
              className="bg-blue-700 hover:bg-blue-800 text-white px-7 rounded-xl"
            >
              Send
            </button>

          </div>

        </div>

      </main>

      <footer className="text-center py-6 text-gray-600">
        StudyBuddy AI • @Bellacancode • 2026
      </footer>

    </div>
  );
}

export default App;