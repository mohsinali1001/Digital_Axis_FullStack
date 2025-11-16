// server.js
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import pool from "./config/db.js";
import authRoutes from "./routes/authRoutes.js";
import apiKeyRoutes from "./routes/apiKeyRoutes.js";
import predictRoutes from "./routes/predictRoutes.js";
import { initSocket } from "./socket.js";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(
  cors({
    origin: ["http://localhost:3000", "http://localhost:5173"], // React frontend URLs
    credentials: true,
  })
);
app.use(express.json());

// Test database connection
pool
  .connect()
  .then((client) => {
    console.log("Database connected successfully");
    client.release(); // release connection back to the pool
  })
  .catch((err) => {
    console.error("Database connection error:", err.stack);
  });

// Routes
app.use("/api/auth", authRoutes);
app.use("/api/apikeys", apiKeyRoutes);
app.use("/api", predictRoutes);

// Test route
app.get("/", (req, res) => {
  res.send("API is running!");
});

// Start server with Socket.IO
const server = app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

// Initialize Socket.IO
initSocket(server);
