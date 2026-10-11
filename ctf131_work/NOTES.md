# 131-two-voices — working notes (unsolved)

Capture: ci8, 1999999 Hz, centre 433.549995 MHz (not the 433.000 on the old sheet).
Only RF content: LoRa, BW 500 kHz, SF7, sync 0x12, 8-symbol preamble, explicit header,
CR 4/5, CRC on, 136-byte payload, one frame per ~65 ms slot (780 frames in 50.7 s).
Voice A (weak, ~25 dB SNR): 5 of every 6 slots.  Voice B (strong, ~+33 dB): every 6th slot.
Payload = b"AL" + 03 05 07 44 + band(0-4) + row(0-127) + 128 pixel bytes  -> 5-band 128x128 imagery.
Strong frames repeat band 0 (and band 3 during t=32..45 s) of the row just sent by the weak voice.
Hidden layer: in strong-minus-weak differences of rows ~84-114 (bands 0 and 3) a 3-line banner:
  line1 "GAIANSPACE{"  line2 ~"TRUE-N?VI-"  line3 ~"HRSTNM}"  (glyphs only partly legible; NOT confirmed)
Decoder: lora.py/full.py (gr-lora_sdr mapping: gray x^(x>>1), deinterleave (i-j-1), data nibble = bit-reversed top 4 bits,
whitening LFSR, CRC16 poly 0x1021 with last-2-byte tweak).
