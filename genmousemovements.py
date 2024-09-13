import random
import math

def simmouse_movements(num_events=100):
    events = []
    for _ in range(num_events):
        event = {
            "clientX": random.randint(0, 1000),
            "clientY": random.randint(0, 1000),
            "movementX": random.randint(-50, 50),
            "movementY": random.randint(-50, 50),
            "screenX": random.randint(0, 1000),
            "screenY": random.randint(0, 1000),
            "timeStamp": random.uniform(0, 5000)
        }
        events.append(event)
    return events

def calculate_mm_md(events):
    max_distance = 0
    prev_event = None
    for event in events:
        if prev_event:
            dx = event["clientX"] - prev_event["clientX"]
            dy = event["clientY"] - prev_event["clientY"]
            distance = math.sqrt(dx**2 + dy**2)
            if distance > max_distance:
                max_distance = distance
        prev_event = event
    return max_distance

def calculate_es_sigmdn(events):
    x = sum(math.log(e["timeStamp"]) for e in events)
    q = len(events)
    y = sum(math.log(e["timeStamp"])**2 for e in events)
    return math.sqrt((q * y - x * x) / (q * (q - 1))) / 1000

def calculate_es_mumdn(events):
    timestamps = [e["timeStamp"] for e in events]
    q = len(events)
    return (sum(timestamps) / q) / 1000

def calculate_es_distmdn(events):
    distances = []
    prev_event = None
    for event in events:
        if prev_event:
            dx = event["clientX"] - prev_event["clientX"]
            dy = event["clientY"] - prev_event["clientY"]
            distances.append(math.sqrt(dx**2 + dy**2))
        prev_event = event
    distances.sort()
    mid = len(distances) // 2
    return distances[mid]

def calculate_es_angsmdn(events):
    start_angles = [random.uniform(-math.pi, math.pi) for _ in events]
    start_angles.sort()
    mid = len(start_angles) // 2
    return start_angles[mid]

def calculate_es_angemdn(events):
    end_angles = [random.uniform(-math.pi, math.pi) for _ in events]
    end_angles.sort()
    mid = len(end_angles) // 2
    return end_angles[mid]

def calculate_event_variables(event_counters):
    m_s_c = event_counters["scroll"]
    m_m_c = event_counters["mousemove"]
    m_c_c = event_counters["click"]

    m_cm_r = m_c_c / m_m_c if m_m_c != 0 else 0
    m_ms_r = m_m_c / m_s_c if m_s_c != 0 else 0

    return {
        "m_s_c": m_s_c,
        "m_m_c": m_m_c,
        "m_c_c": m_c_c,
        "m_cm_r": m_cm_r,
        "m_ms_r": m_ms_r
    }
def generate_mouse_movements():
    mouse_events = simmouse_movements()

    mm_md = calculate_mm_md(mouse_events)
    es_sigmdn = calculate_es_sigmdn(mouse_events)
    es_mumdn = calculate_es_mumdn(mouse_events)
    es_distmdn = calculate_es_distmdn(mouse_events)
    es_angsmdn = calculate_es_angsmdn(mouse_events)
    es_angemdn = calculate_es_angemdn(mouse_events)


    # Change depending on device/use touch if automating on mobile user agent
    event_counters = {
        "mousemove": len(mouse_events),
        "click": random.randint(0, 10),
        "scroll": random.randint(0, 600),
        "touchstart": 0,
        "touchend": 0,
        "touchmove": 0,
        "keydown": 0,
        "keyup": 0
    }
    event_vars = calculate_event_variables(event_counters)

    return {
        "mp_cx": random.choice(mouse_events)["clientX"],
        "mp_cy": random.choice(mouse_events)["clientY"],
        "mm_md": mm_md,
        "es_sigmdn": es_sigmdn,
        "es_mumdn": es_mumdn,
        "es_distmdn": es_distmdn,
        "es_angsmdn": es_angsmdn,
        "es_angemdn": es_angemdn,
        **event_vars
    }
