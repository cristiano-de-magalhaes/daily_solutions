import mlx_whisper
import json
from pathlib import Path


def transcrever_audio(
    caminho_audio: str,
    modelo: str = "mlx-community/whisper-large-v3-turbo",
    mostrar_timestamps: bool = True,
) -> dict:
    """
    Transcreve um arquivo de áudio em português do Brasil usando MLX Whisper.

    Args:
        caminho_audio: Caminho para o arquivo de áudio (.mp3, .wav, .m4a, etc.)
        modelo: Modelo Whisper a ser usado
        mostrar_timestamps: Se True, exibe timestamps de cada segmento

    Returns:
        Dicionário com a transcrição completa e segmentos
    """
    audio = Path(caminho_audio)
    if not audio.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_audio}")

    print(f"🎙️  Transcrevendo: {audio.name}")
    print(f"📦 Modelo: {modelo}\n")

    resultado = mlx_whisper.transcribe(
        str(audio),
        path_or_hf_repo=modelo,
        language="pt",           # Português
        task="transcribe",       # "transcribe" mantém o idioma original
        word_timestamps=True,    # Timestamps por palavra (útil para múltiplos falantes)
        verbose=False,
    )

    return resultado


def formatar_transcricao(resultado: dict, mostrar_timestamps: bool = True) -> str:
    """
    Formata a transcrição com timestamps e segmentos bem organizados.

    Args:
        resultado: Dicionário retornado pelo mlx_whisper.transcribe()
        mostrar_timestamps: Se True, inclui timestamps nos segmentos

    Returns:
        String formatada com a transcrição
    """
    linhas = []
    linhas.append("=" * 60)
    linhas.append("📝 TRANSCRIÇÃO COMPLETA")
    linhas.append("=" * 60)
    linhas.append(resultado.get("text", "").strip())
    linhas.append("")

    if mostrar_timestamps and "segments" in resultado:
        linhas.append("=" * 60)
        linhas.append("⏱️  SEGMENTOS COM TIMESTAMPS")
        linhas.append("=" * 60)

        for i, segmento in enumerate(resultado["segments"], start=1):
            inicio = formatar_tempo(segmento["start"])
            fim    = formatar_tempo(segmento["end"])
            texto  = segmento["text"].strip()

            linhas.append(f"[{i:03d}] {inicio} → {fim}")
            linhas.append(f"      {texto}")
            linhas.append("")

    return "\n".join(linhas)


def formatar_tempo(segundos: float) -> str:
    """Converte segundos em formato HH:MM:SS,mmm."""
    horas   = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segs    = int(segundos % 60)
    millis  = int((segundos % 1) * 1000)
    return f"{horas:02d}:{minutos:02d}:{segs:02d},{millis:03d}"


def salvar_resultados(resultado: dict, caminho_base: str) -> None:
    """
    Salva a transcrição em três formatos:
      - .txt  → texto puro
      - .json → dados completos (segmentos, confiança, etc.)
      - .srt  → legendas no formato SubRip
    """
    base = Path(caminho_base).stem

    # --- TXT ---
    with open(f"{base}_transcricao.txt", "w", encoding="utf-8") as f:
        f.write(resultado.get("text", "").strip())
    print(f"✅ TXT salvo:  {base}_transcricao.txt")

    # --- JSON ---
    with open(f"{base}_transcricao.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON salvo: {base}_transcricao.json")

    # --- SRT ---
    with open(f"{base}_transcricao.srt", "w", encoding="utf-8") as f:
        for i, seg in enumerate(resultado.get("segments", []), start=1):
            inicio = formatar_tempo(seg["start"]).replace(",", ",")
            fim    = formatar_tempo(seg["end"]).replace(",", ",")
            texto  = seg["text"].strip()
            f.write(f"{i}\n{inicio} --> {fim}\n{texto}\n\n")
    print(f"✅ SRT salvo:  {base}_transcricao.srt")


# ─────────────────────────────────────────────
#  PONTO DE ENTRADA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ARQUIVO_AUDIO = "reuniao.mp3"   # ← altere para o seu arquivo
    ARQUIVO_AUDIO = "/Users/fo094511/_PROJETOS_VSCODE/daily_solutions/daily_solutions/OTHER FILES/Onboarding com time de Dados.m4a"   # ← altere para o seu arquivo

    # Modelos disponíveis (do mais rápido ao mais preciso):
    #   mlx-community/whisper-tiny
    #   mlx-community/whisper-base
    #   mlx-community/whisper-small
    #   mlx-community/whisper-medium
    #   mlx-community/whisper-large-v3
    #   mlx-community/whisper-large-v3-turbo   ← melhor custo-benefício
    MODELO = "mlx-community/whisper-large-v3-turbo"

    resultado = transcrever_audio(
        caminho_audio=ARQUIVO_AUDIO,
        modelo=MODELO,
        mostrar_timestamps=True,
    )

    transcricao_formatada = formatar_transcricao(resultado, mostrar_timestamps=True)
    print(transcricao_formatada)

    salvar_resultados(resultado, ARQUIVO_AUDIO)