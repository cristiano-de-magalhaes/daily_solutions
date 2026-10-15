from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token="SEU_TOKEN_HUGGINGFACE",  # huggingface.co/settings/tokens
)

diarizacao = pipeline("reuniao.mp3")

for turno, _, falante in diarizacao.itertracks(yield_label=True):
    print(f"[{falante}] {turno.start:.1f}s → {turno.end:.1f}s")