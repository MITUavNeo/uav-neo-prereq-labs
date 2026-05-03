"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Final Challenge
Purpose: Orchestrates 4 challenges sequentially. Each challenge module exposes:
    reset()              — initialise / re-initialise the challenge
    update(drone) → bool — run one frame, return True when complete

Challenges:
    1. Hoop Race      — fly through 4 altitude-varying gates
    2. False Wall     — ArUco marker maze (ID 0=fake, 1=real, 2=end)
    3. Distance Maze  — right-hand-rule navigation
    4. Search & Rescue — spiral search + land on magenta target

A per-challenge timeout (CHALLENGE_TIMEOUT seconds) prevents getting stuck.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))

import drone_core
from final_tasks import challenge1_hoop_race
from final_tasks import challenge2_false_wall
from final_tasks import challenge3_distance_maze
from final_tasks import challenge4_sar

# ── Configuration ──────────────────────────────────────────────────────────────
TAKEOFF_ALT       = 1.5    # m — competition altitude
TAKEOFF_WAIT      = 3.5    # s — wait for motors to spool up
CHALLENGE_TIMEOUT = 120.0  # s — skip a challenge if it exceeds this

_CHALLENGES = [
    ("Hoop Race",       challenge1_hoop_race),
    ("False Wall",      challenge2_false_wall),
    ("Distance Maze",   challenge3_distance_maze),
    ("Search & Rescue", challenge4_sar),
]

# ── Module-level state ─────────────────────────────────────────────────────────
_drone       = drone_core.create_drone()
_init_phase  = 0       # 0=takeoff wait, 1=altitude adjust
_init_timer  = 0.0
_ch_index    = 0       # 0=initialising, 1..4=running challenge, >4=all done
_ch_timer    = 0.0
_ch_results  = {}      # {name: (success: bool, elapsed: float)}

# ──────────────────────────────────────────────────────────────────────────────


def start():
    global _init_phase, _init_timer, _ch_index, _ch_timer, _ch_results
    _init_phase = 0; _init_timer = 0.0
    _ch_index   = 0; _ch_timer   = 0.0
    _ch_results = {}
    for _, ch in _CHALLENGES:
        ch.reset()
    print("=== Beaver Warrior Final Challenge — Starting ===")


def update():
    global _init_phase, _init_timer, _ch_index, _ch_timer

    # ── Step 0: Takeoff and reach competition altitude ─────────────────────────
    if _ch_index == 0:
        _init_timer += _drone.get_delta_time()
        if _init_phase == 0:
            _drone.flight.takeoff()
            if _init_timer >= TAKEOFF_WAIT:
                _init_phase = 1; _init_timer = 0.0
        else:
            err = TAKEOFF_ALT - _drone.physics.get_altitude()
            if abs(err) < 0.12:
                _drone.flight.stop()
                print(f"[Final] Ready at {_drone.physics.get_altitude():.2f} m")
                print(f"[Final] Starting Challenge 1: {_CHALLENGES[0][0]}")
                _ch_index = 1; _ch_timer = 0.0
            else:
                thr = max(-0.5, min(0.5, err * 2.5))
                _drone.flight.send_pcmd(0, 0, 0, thr)
        return

    # ── All challenges complete ────────────────────────────────────────────────
    if _ch_index > len(_CHALLENGES):
        _drone.flight.stop()
        return

    # ── Run current challenge ──────────────────────────────────────────────────
    ci        = _ch_index - 1
    name, ch  = _CHALLENGES[ci]
    _ch_timer += _drone.get_delta_time()

    # Timeout guard
    if _ch_timer > CHALLENGE_TIMEOUT:
        print(f"[Final] TIMEOUT — {name} (>{CHALLENGE_TIMEOUT:.0f} s)")
        _ch_results[name] = (False, _ch_timer)
        _advance_challenge()
        return

    done = ch.update(_drone)
    if done:
        print(f"[Final] {name} COMPLETE in {_ch_timer:.1f} s")
        _ch_results[name] = (True, _ch_timer)
        _advance_challenge()


def _advance_challenge():
    global _ch_index, _ch_timer
    _ch_index += 1; _ch_timer = 0.0
    if _ch_index <= len(_CHALLENGES):
        name, ch = _CHALLENGES[_ch_index - 1]
        ch.reset()
        print(f"[Final] Starting Challenge {_ch_index}: {name}")
    else:
        _print_results()
        _drone.flight.stop()


def _print_results():
    print("\n=== BEAVER WARRIOR RESULTS ===")
    for name, (success, t) in _ch_results.items():
        status = "PASS" if success else "FAIL/TIMEOUT"
        print(f"  {name:<22}: {status}  ({t:.1f} s)")
    print("==============================\n")


def update_slow():
    if 1 <= _ch_index <= len(_CHALLENGES):
        name, _ = _CHALLENGES[_ch_index - 1]
        alt     = _drone.physics.get_altitude()
        print(f"[Final] Ch{_ch_index} ({name}) — alt={alt:.2f}m  t={_ch_timer:.1f}s")


_drone.set_start_update_slow(start, update, update_slow)
_drone.go()
