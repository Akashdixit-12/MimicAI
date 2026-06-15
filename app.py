import gradio as gr
from f5_tts.api import F5TTS

tts = F5TTS()

def generate_voice(ref_audio, ref_text, gen_text):
    try:
        wav, sr, spect = tts.infer(
            ref_file=ref_audio,
            ref_text=ref_text,
            gen_text=gen_text
        )

        output_file = "output.wav"

        import soundfile as sf
        sf.write(output_file, wav, sr)

        return output_file

    except Exception as e:
        return str(e)


with gr.Blocks(title="MIMICAI") as demo:

    gr.Markdown("# 🎙️ MIMICAI")
    gr.Markdown("Voice Cloning using F5-TTS")

    ref_audio = gr.Audio(
        label="Reference Audio",
        type="filepath"
    )

    ref_text = gr.Textbox(
        label="Reference Text"
    )

    gen_text = gr.Textbox(
        label="Text To Generate"
    )

    output_audio = gr.Audio(
        label="Generated Audio"
    )

    btn = gr.Button("Generate Voice")

    btn.click(
        fn=generate_voice,
        inputs=[ref_audio, ref_text, gen_text],
        outputs=output_audio
    )

demo.launch()