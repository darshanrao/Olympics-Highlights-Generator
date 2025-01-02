
# Olympic Highlight Generator

Revolutionizing sports highlight creation with the power of AI! Whether you're a broadcaster or content creator, our solution delivers engaging Olympic moments from a simple prompt. 

---

## 🌟 Inspiration

The 2024 Summer Olympics is a global event, watched by millions worldwide. Traditional highlight generation is time-consuming and requires manual editing. We sought to create a tool that:  
- Enables fans, broadcasters, and content creators to relive thrilling Olympic moments.  
- Streamlines the production of personalized and professional-quality sports highlights.  
Our goal is to empower producers with AI to create engaging commentary and visuals tailored to consumer interests.

---

## 🎯 What It Does

The **Olympic Highlight Generator** creates dynamic highlight reels from user prompts.  
Key features:  
1. Takes a natural language prompt as input.  
2. Extracts relevant Olympic footage using AI-powered video search.  
3. Generates an engaging script contextualized to the selected clips.  
4. Converts the script into a realistic voice-over.  
5. Automatically edits visuals to synchronize with the generated narration.  

The result? **90-second professional-quality highlight reels** delivered seamlessly.  

---

## 🛠️ How We Built It

Our project integrates multiple AI models and APIs in a unified workflow:  
1. **Video Search**: User prompts guide the Marengo model (TwelveLabs) to extract relevant Olympic clips from a curated database.  
2. **Script Generation**: The Pegasus model generates commentary tailored to the video context.  
3. **Text-to-Speech**: ElevenLabs' API creates lifelike voice-overs from the script.  
4. **Video Editing**: A custom algorithm aligns visuals with narration, ensuring perfect synchronization.  
5. **Web Interface**: A user-friendly platform allows seamless interaction with the system.  

---

## 🚧 Challenges We Faced

- Ensuring generated scripts align with available Olympic footage.  
- Synchronizing visuals with AI-generated voice-overs required meticulous model fine-tuning.  
- Handling the integration of multiple API calls into a seamless pipeline.  

---

## 🏆 Accomplishments

- Fully automated a traditionally manual, labor-intensive process of highlight generation.  
- Achieved high-quality voice-overs synchronized perfectly with footage.  
- Created a scalable, user-friendly web platform.  

---

## 📚 What We Learned

- Advanced video editing and synchronization with AI-generated scripts.  
- Integrating diverse APIs into a cohesive pipeline.  
- Tackling unique challenges associated with working with Olympic footage.  

---

## 🚀 What's Next

- **Live Event Highlights**: Support real-time highlight generation during live Olympic broadcasts.  
- **Enhanced Personalization**: Adjust tone, emphasize specific athletes or events, and more.  
- **Expand Video Index**: Include a broader range of sports and other global events.  

---

## 🖥️ Tech Stack

- **Frontend**: React.js (for user interaction)  
- **Backend**: Node.js, Express.js (for API calls and integrations)  
- **AI Models**:  
  - Marengo (TwelveLabs): Video search and clip extraction.  
  - Pegasus: Script generation.  
  - ElevenLabs: Text-to-speech voice-over.  
- **Video Editing**: Custom Python algorithm for synchronization.  
- **Hosting**: Deployed on [insert platform].  

---

## 🚀 Getting Started

### Prerequisites
1. Node.js installed (`>=v16.x`).  
2. Python 3.8 or higher installed.  
3. API keys for TwelveLabs, ElevenLabs, and Google Cloud.  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/username/olympic-highlight-generator.git
   cd olympic-highlight-generator
   ```  
2. Install dependencies for the backend:  
   ```bash
   cd backend
   npm install
   ```  
3. Install dependencies for the frontend:  
   ```bash
   cd ../frontend
   npm install
   ```  
4. Install Python requirements:  
   ```bash
   pip install -r requirements.txt
   ```  

### Running the Project  
1. Start the backend:  
   ```bash
   cd backend
   npm start
   ```  
2. Start the frontend:  
   ```bash
   cd ../frontend
   npm start
   ```  

---

## 🤝 Contributing

We welcome contributions!  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes and push to the branch:  
   ```bash
   git push origin feature-name
   ```  
4. Open a Pull Request.  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  

---

## 🏅 Team

- **Darshan Rao**: Backend development and system integration.  
- **[Other Team Members]**: Roles and contributions.  

---

## ✨ Demo

[Insert link to a live demo or a video showcasing the project.]  

---

We hope you enjoy using **Olympic Highlight Generator** as much as we enjoyed building it! For feedback or questions, feel free to reach out.  
