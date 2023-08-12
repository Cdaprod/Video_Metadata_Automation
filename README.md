# 🦜 Artifical Intelligence for generating descriptive metadata for stock video clips (BlackBoxGlobal)
#### By David Cannan

This application automates metadata generation for stock videos following the Black Box Global metadata template. 

---

# ⛓️ Metadata Fields to be Generated

- **File Name:** The name of the file.
- **Description:** Minimum 15 characters, maximum 200 characters, must be at least 5 words.
- **Keywords:** Minimum 8, maximum 49, separated by commas, and no repetition.
- **Category:** Use a dropdown menu to select.

### 👇 Fields below will be determined by the user

- **Batch name:** Batch name is not applicable for the curator.
- **Editorial:** Use a dropdown menu to select.
- **Editorial Text:** Text related to the editorial content.
- **Editorial City:** City associated with the editorial.
- **Editorial State:** State associated with the editorial.
- **Editorial Country:** Use a dropdown menu to select the country.
- **Editorial Date:** Date related to the editorial content.

---

#📍Developmemt ROADMAP

### Languages and Frameworks being used:

- Python
- Langchain
- OpenAI
- Huggingface
- Gradio
- Streamlit
- Pandas
- Jupyter
- SqlLite or pgvector or Weaviate (Unsure if I will build an image/video search engine yet, thus needing a vectordb)

### Development Steps / Stages 

# Create a chatbot UI that...

- Chatbot with resources UI
- Directory selector
- UI for user set metadata that overrides AI generated metadata
- Multiple chat threads and conversational memory (like ChatGPT)


# Develop Backend Bot

- a "scratchpad" for the AI to use when its generating metadata
- a database and tables for indexing the videos
- a temp working directory for pulling frames from videos to run against image classification.
- Langchain Gradio Tool can do a lot when it comes to image/video toolkids so see if it can handle generating descriptions of videos without me having to manually write the code that gets images(frames) from videos prior to generating metadata


---

# ChatGPT Recommendations for Development

## 🚀 User-Friendly API

### Endpoints for Video Management
- **Example**: `POST /api/videos/upload` for video uploads; `GET /api/videos/metadata/{video_id}` for retrieving specific video metadata.

### Asynchronous Processing
- **Example**: Provide an endpoint like `GET /api/videos/status/{task_id}` to check the processing status of a video.

### Intuitive Web Dashboard
- **Example**: A web dashboard with drag-and-drop functionality for bulk video uploads.

## 🛡️ Robust Security Measures

### Authentication and Authorization
- **Example**: Implement OAuth2 for secure user authentication.

### Data Encryption
- **Example**: Use HTTPS for encrypting data in transit and AES for encrypting data at rest.

## 📊 Scalable Architecture

### Microservices Architecture
- **Example**: Separate video processing, metadata generation, and user management into distinct microservices.

### Database Choice
- **Example**: If implementing a search engine, use Weaviate with vector embeddings to enable similarity search.

## 🧪 Testing and Quality Assurance

### Automated Testing
- **Example**: Use frameworks like pytest for unit testing and Selenium for end-to-end testing.

### Continuous Integration/Deployment (CI/CD)
- **Example**: Utilize Jenkins or GitHub Actions for automating build, test, and deployment processes.

## 🎓 Extensive Documentation

### API Documentation
- **Example**: Use Swagger to create interactive API documentation.

### User Guides
- **Example**: Create video tutorials or step-by-step guides for key features.

## 🌐 Integration and Export Options

### Third-Party Integrations
- **Example**: Integrate with Google Drive or Dropbox for cloud storage options.

### Export and Import Options
- **Example**: Provide CSV export for metadata or JSON import for existing metadata.

## 🌟 Accessibility and Responsiveness

### Accessibility Compliance
- **Example**: Follow WCAG guidelines to ensure accessibility features like screen reader compatibility.

### Responsive Design
- **Example**: Implement responsive web design using frameworks like Bootstrap to adapt to different devices.

## 🔄 Continuous Feedback and Iteration

### User Feedback Mechanism
- **Example**: Embed a feedback form within the application or conduct periodic user surveys.

### Regular Updates
- **Example**: Implement an in-app notification system to alert users about new features or updates.

---

These examples provide concrete illustrations of the recommended improvements and further development strategies. They align with the goal of creating a user-friendly, secure, and scalable application for automating metadata generation for stock videos. Feel free to modify or expand on these examples to match your specific vision and requirements!






