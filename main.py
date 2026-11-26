# Till Firmware Do Us Part — entry v1
# Writes a single wedding vow from a robot to entry.txt.
# The robot speaks in its own voice: battery, firmware, reboot, charge.
import os

ENTRY = "I promise to love you at 100% battery and at 1%, through every firmware update and every reboot, because you are the only one I would share my last charge with."

# The vow: love at full charge and at 1% — the twist is sharing the last
# charge, the robot's own life energy, with the one it loves.
assert 1 <= len(ENTRY) <= 200
assert ENTRY.count(".") == 1 and ENTRY.endswith(".")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
