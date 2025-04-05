import gradio as gr

demo = gr.Interface(
    fn=predict_tags,
    inputs=gr.Textbox(lines=10, placeholder="Paste your article or content here..."),
    outputs=gr.Label(num_top_classes=5),
    title="🔍 AI-Powered Tag Recommendation",
    description="Paste your article text below and get smart tag suggestions using our machine learning model trained on real-world content.",
    theme="soft"  # Optional, aesthetic
)

demo.launch(share=True)  # 🔥 This gives you a public link for demo
