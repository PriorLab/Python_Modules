#!/bin/bash
# =============================================================
#  Python Module 02 — Garden Guardian (Exception Handling)
#  Deep tester — covers all exercises + evaluation sheet checks
#  Usage: bash tester_mod02.sh /path/to/student/repo
# =============================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
BOLD='\033[1m'
RESET='\033[0m'

pass=0
fail=0
warn=0

ok()   { echo -e "  ${GREEN}[OK]${RESET}   $1"; pass=$((pass+1)); }
ko()   { echo -e "  ${RED}[KO]${RESET}   $1"; fail=$((fail+1)); }
wa()   { echo -e "  ${YELLOW}[!!]${RESET}   $1"; warn=$((warn+1)); }
hdr()  {
    echo ""
    echo -e "${BOLD}${CYAN}══════════════════════════════════════${RESET}"
    echo -e "${BOLD}${CYAN}  $1${RESET}"
    echo -e "${BOLD}${CYAN}══════════════════════════════════════${RESET}"
}
info() { echo -e "  ${MAGENTA}[>>]${RESET}   $1"; }

# ── Args ──────────────────────────────────────────────────────
REPO="${1:-$(pwd)}"
echo -e "${BOLD}${CYAN}"
echo "╔══════════════════════════════════════╗"
echo "║   Python Module 02 — Deep Tester     ║"
echo "╚══════════════════════════════════════╝"
echo -e "${RESET}"
echo -e "Repo: ${BOLD}$REPO${RESET}"

# ── Helpers ───────────────────────────────────────────────────
run_py() {
    timeout 5 python3 "$@" 2>&1
}

check_output() {
    local label="$1"
    local output="$2"
    local pattern="$3"
    if echo "$output" | grep -qE "$pattern"; then
        ok "$label"
    else
        ko "$label"
        info "Expected pattern: $pattern"
        info "Got: $(echo "$output" | head -5)"
    fi
}

check_no_crash() {
    local label="$1"
    local file="$2"
    local out
    out=$(run_py "$file" 2>&1)
    local exit_code=$?
    if [ $exit_code -eq 124 ]; then
        ko "$label — TIMEOUT (infinite loop?)"
    elif echo "$out" | grep -qiE "Traceback|SyntaxError|NameError|AttributeError"; then
        ko "$label — CRASHED"
        info "$(echo "$out" | head -3)"
    else
        ok "$label — no crash"
    fi
}

check_flake8() {
    local file="$1"
    local out
    out=$(python3 -m flake8 "$file" 2>&1)
    if [ -z "$out" ]; then
        ok "flake8: no errors"
    else
        ko "flake8 errors:"
        echo "$out" | head -10 | sed 's/^/    /'
    fi
}

check_mypy() {
    local file="$1"
    local out
    out=$(python3 -m mypy "$file" --ignore-missing-imports 2>&1)
    if echo "$out" | grep -q "Success"; then
        ok "mypy: no errors"
    else
        # Check if the only errors are the intentional TypeError one
        local errors
        errors=$(echo "$out" | grep "error:" | grep -v "Unsupported operand\|str.*int\|int.*str" | head -5)
        if [ -z "$errors" ]; then
            ok "mypy: only expected errors (intentional TypeError in ex2)"
        else
            ko "mypy errors:"
            echo "$errors" | sed 's/^/    /'
        fi
    fi
}

check_type_hints() {
    local file="$1"
    local out
    out=$(python3 -c "
import ast, sys
with open('$file') as f:
    tree = ast.parse(f.read())
missing = []
for node in ast.walk(tree):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        if node.name == '__init__':
            continue
        has_return = node.returns is not None
        args_annotated = all(
            a.annotation is not None
            for a in node.args.args
            if a.arg != 'self'
        )
        if not has_return or not args_annotated:
            missing.append(node.name)
if missing:
    print('Missing type hints:', ', '.join(missing))
else:
    print('OK')
" 2>&1)
    if echo "$out" | grep -q "^OK"; then
        ok "type hints present"
    else
        ko "type hints: $out"
    fi
}

file_exists() {
    local path="$1"
    local label="$2"
    if [ -f "$path" ]; then
        ok "file exists: $label"
        return 0
    else
        ko "file MISSING: $label"
        return 1
    fi
}

# ── Install tools if needed ───────────────────────────────────
python3 -m flake8 --version &>/dev/null || pip install flake8 --break-system-packages -q
python3 -m mypy --version &>/dev/null   || pip install mypy  --break-system-packages -q

# ═══════════════════════════════════════════════════════════════
hdr "FILES — Required structure"
# ═══════════════════════════════════════════════════════════════

EX0="$REPO/ex0/ft_first_exception.py"
EX1="$REPO/ex1/ft_raise_exception.py"
EX2="$REPO/ex2/ft_different_errors.py"
EX3="$REPO/ex3/ft_custom_errors.py"
EX4="$REPO/ex4/ft_finally_block.py"

file_exists "$EX0" "ex0/ft_first_exception.py"
file_exists "$EX1" "ex1/ft_raise_exception.py"
file_exists "$EX2" "ex2/ft_different_errors.py"
file_exists "$EX3" "ex3/ft_custom_errors.py"
file_exists "$EX4" "ex4/ft_finally_block.py"

# Check no extra unauthorized files
for ex in ex0 ex1 ex2 ex3 ex4; do
    dir="$REPO/$ex"
    [ -d "$dir" ] || continue
    extras=$(find "$dir" -name "*.py" | grep -v "ft_first_exception\|ft_raise_exception\|ft_different_errors\|ft_custom_errors\|ft_finally_block" | wc -l)
    if [ "$extras" -gt 0 ]; then
        wa "$ex/: extra .py files found (check if authorized)"
    fi
done

# ═══════════════════════════════════════════════════════════════
hdr "EX0 — ft_first_exception.py"
# ═══════════════════════════════════════════════════════════════

if [ -f "$EX0" ]; then
    OUT=$(run_py "$EX0")

    check_flake8 "$EX0"
    check_mypy "$EX0"
    check_type_hints "$EX0"
    check_no_crash "program runs without crash" "$EX0"

    # Structure checks
    if grep -q "if __name__" "$EX0"; then
        ok "uses if __name__ == '__main__'"
    else
        ko "missing if __name__ == '__main__'"
    fi

    if grep -qE "def input_temperature" "$EX0"; then
        ok "function input_temperature() defined"
    else
        ko "function input_temperature() missing"
    fi

    if grep -qE "def test_temperature" "$EX0"; then
        ok "function test_temperature() defined"
    else
        ko "function test_temperature() missing"
    fi

    if grep -qE "try\s*:" "$EX0"; then
        ok "uses try block"
    else
        ko "no try block found"
    fi

    if grep -qE "except" "$EX0"; then
        ok "uses except"
    else
        ko "no except found"
    fi

    # Output checks
    check_output "prints header '=== Garden Temperature'"   "$OUT" "Garden Temperature"
    check_output "mentions input '25'"                      "$OUT" "25"
    check_output "prints 'Temperature is now 25'"           "$OUT" "Temperature is now 25"
    check_output "mentions input 'abc'"                     "$OUT" "abc"
    check_output "catches error for 'abc'"                  "$OUT" "Caught input_temperature error"
    check_output "prints 'invalid literal' in error"        "$OUT" "invalid literal"
    check_output "prints 'didn't crash' at end"             "$OUT" "didn.t crash|didn't crash"

    # int() conversion check
    out_int=$(python3 -c "
import sys
sys.path.insert(0, '$(dirname $EX0)')
import importlib.util
spec = importlib.util.spec_from_file_location('m', '$EX0')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
result = m.input_temperature('42')
print(type(result).__name__, result)
" 2>&1)
    if echo "$out_int" | grep -q "^int 42"; then
        ok "input_temperature('42') returns int 42"
    else
        ko "input_temperature('42') should return int 42 — got: $out_int"
    fi

    # Exception for invalid input
    out_exc=$(python3 -c "
import sys
sys.path.insert(0, '$(dirname $EX0)')
import importlib.util
spec = importlib.util.spec_from_file_location('m', '$EX0')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
try:
    m.input_temperature('abc')
    print('NO_EXCEPTION')
except Exception as e:
    print('EXCEPTION:', type(e).__name__)
" 2>&1)
    if echo "$out_exc" | grep -q "EXCEPTION:"; then
        ok "input_temperature('abc') raises an exception"
    else
        ko "input_temperature('abc') should raise exception"
    fi
fi

# ═══════════════════════════════════════════════════════════════
hdr "EX1 — ft_raise_exception.py"
# ═══════════════════════════════════════════════════════════════

if [ -f "$EX1" ]; then
    OUT=$(run_py "$EX1")

    check_flake8 "$EX1"
    check_mypy "$EX1"
    check_type_hints "$EX1"
    check_no_crash "program runs without crash" "$EX1"

    if grep -qE "raise" "$EX1"; then
        ok "uses raise"
    else
        ko "no raise found — must raise exception for invalid temps"
    fi

    if grep -qE "try\s*:|except" "$EX1"; then
        ok "uses try/except"
    else
        ko "no try/except found"
    fi

    # Output checks
    check_output "valid temp '25' accepted"             "$OUT" "Temperature is now 25"
    check_output "invalid 'abc' caught"                 "$OUT" "Caught input_temperature error.*invalid literal|invalid literal.*abc"
    check_output "'100' rejected as too hot"            "$OUT" "too hot|100.*max|max.*40"
    check_output "'-50' rejected as too cold"           "$OUT" "too cold|-50.*min|min.*0"
    check_output "program completes without crash"      "$OUT" "didn.t crash|didn't crash|completed"

    # Function logic checks via import
    result=$(python3 -c "
import importlib.util
spec = importlib.util.spec_from_file_location('m', '$EX1')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

results = []

# Valid range
try:
    r = m.input_temperature('0')
    results.append('0:' + str(r))
except Exception as e:
    results.append('0:RAISED:' + str(e))

try:
    r = m.input_temperature('40')
    results.append('40:' + str(r))
except Exception as e:
    results.append('40:RAISED:' + str(e))

# Invalid range
try:
    m.input_temperature('41')
    results.append('41:NO_RAISE')
except Exception:
    results.append('41:RAISED_OK')

try:
    m.input_temperature('-1')
    results.append('-1:NO_RAISE')
except Exception:
    results.append('-1:RAISED_OK')

try:
    m.input_temperature('100')
    results.append('100:NO_RAISE')
except Exception:
    results.append('100:RAISED_OK')

try:
    m.input_temperature('-50')
    results.append('-50:NO_RAISE')
except Exception:
    results.append('-50:RAISED_OK')

print('\n'.join(results))
" 2>&1)

    echo "$result" | grep -q "0:0"   && ok "input_temperature('0') returns 0 (boundary OK)"   || ko "input_temperature('0') should return 0"
    echo "$result" | grep -q "40:40" && ok "input_temperature('40') returns 40 (boundary OK)"  || ko "input_temperature('40') should return 40"
    echo "$result" | grep -q "41:RAISED_OK"  && ok "input_temperature('41') raises (too hot)"  || ko "input_temperature('41') should raise"
    echo "$result" | grep -q "\-1:RAISED_OK" && ok "input_temperature('-1') raises (too cold)"  || ko "input_temperature('-1') should raise"
    echo "$result" | grep -q "100:RAISED_OK" && ok "input_temperature('100') raises"            || ko "input_temperature('100') should raise"
    echo "$result" | grep -q "\-50:RAISED_OK" && ok "input_temperature('-50') raises"           || ko "input_temperature('-50') should raise"
fi

# ═══════════════════════════════════════════════════════════════
hdr "EX2 — ft_different_errors.py"
# ═══════════════════════════════════════════════════════════════

if [ -f "$EX2" ]; then
    OUT=$(run_py "$EX2")

    check_flake8 "$EX2"
    check_no_crash "program runs without crash" "$EX2"

    # mypy special — TypeError is intentional
    MYPY_OUT=$(python3 -m mypy "$EX2" --ignore-missing-imports 2>&1)
    if echo "$MYPY_OUT" | grep "error:" | grep -vqE "Unsupported operand|str.*int|int.*str|Cannot add"; then
        ok "mypy: only expected errors"
    else
        EXTRA=$(echo "$MYPY_OUT" | grep "error:" | grep -vE "Unsupported operand|str.*int|int.*str|Cannot add")
        if [ -n "$EXTRA" ]; then
            ko "mypy unexpected errors: $EXTRA"
        else
            ok "mypy: only expected errors"
        fi
    fi

    if grep -qE "def garden_operations" "$EX2"; then
        ok "function garden_operations() defined"
    else
        ko "function garden_operations() missing"
    fi

    if grep -qE "def test_error_types" "$EX2"; then
        ok "function test_error_types() defined"
    else
        ko "function test_error_types() missing"
    fi

    # Output checks — 4 error types
    check_output "ValueError caught"        "$OUT" "ValueError"
    check_output "ZeroDivisionError caught" "$OUT" "ZeroDivisionError"
    check_output "FileNotFoundError caught" "$OUT" "FileNotFoundError"
    check_output "TypeError caught"         "$OUT" "TypeError"
    check_output "operation 4 succeeds"     "$OUT" "Operation completed|success|completed"

    # Verify each operation raises the right exception
    result=$(python3 -c "
import importlib.util
spec = importlib.util.spec_from_file_location('m', '$EX2')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

tests = {0: 'ValueError', 1: 'ZeroDivisionError', 2: 'FileNotFoundError', 3: 'TypeError'}
for op, expected in tests.items():
    try:
        m.garden_operations(op)
        print(f'{op}:NO_RAISE (expected {expected})')
    except Exception as e:
        got = type(e).__name__
        if got == expected:
            print(f'{op}:OK:{got}')
        else:
            print(f'{op}:WRONG_TYPE:{got} (expected {expected})')
" 2>&1)

    echo "$result" | grep -q "0:OK:ValueError"          && ok "op 0 raises ValueError"          || ko "op 0 should raise ValueError — got: $(echo "$result" | grep '^0:')"
    echo "$result" | grep -q "1:OK:ZeroDivisionError"   && ok "op 1 raises ZeroDivisionError"   || ko "op 1 should raise ZeroDivisionError"
    echo "$result" | grep -q "2:OK:FileNotFoundError"   && ok "op 2 raises FileNotFoundError"   || ko "op 2 should raise FileNotFoundError"
    echo "$result" | grep -q "3:OK:TypeError"           && ok "op 3 raises TypeError"           || ko "op 3 should raise TypeError"

    # op 4 should NOT raise
    result4=$(python3 -c "
import importlib.util
spec = importlib.util.spec_from_file_location('m', '$EX2')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
try:
    m.garden_operations(4)
    print('OK')
except Exception as e:
    print('RAISED:', e)
" 2>&1)
    echo "$result4" | grep -q "^OK" && ok "op 4 completes without exception" || ko "op 4 should not raise — got: $result4"

    # Check catching multiple errors with single try
    if python3 -c "
import ast
with open('$EX2') as f:
    tree = ast.parse(f.read())
for node in ast.walk(tree):
    if isinstance(node, ast.ExceptHandler):
        if isinstance(node.type, ast.Tuple) and len(node.type.elts) > 1:
            print('MULTI_EXCEPT')
            break
" 2>&1 | grep -q "MULTI_EXCEPT"; then
        ok "catches multiple error types with single except"
    else
        wa "no 'except (A, B)' pattern found — subject asks to demonstrate this"
    fi
fi

# ═══════════════════════════════════════════════════════════════
hdr "EX3 — ft_custom_errors.py"
# ═══════════════════════════════════════════════════════════════

if [ -f "$EX3" ]; then
    OUT=$(run_py "$EX3")

    check_flake8 "$EX3"
    check_mypy "$EX3"
    check_type_hints "$EX3"
    check_no_crash "program runs without crash" "$EX3"

    # Class structure checks
    for cls in GardenError PlantError WaterError; do
        if grep -qE "class $cls" "$EX3"; then
            ok "class $cls defined"
        else
            ko "class $cls missing"
        fi
    done

    # Inheritance checks via import
    result=$(python3 -c "
import importlib.util
spec = importlib.util.spec_from_file_location('m', '$EX3')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# Inheritance chain
print('GardenError->Exception:', issubclass(m.GardenError, Exception))
print('PlantError->GardenError:', issubclass(m.PlantError, m.GardenError))
print('WaterError->GardenError:', issubclass(m.WaterError, m.GardenError))

# Default messages
try:
    raise m.PlantError()
except m.PlantError as e:
    print('PlantError default msg:', str(e) != '')

try:
    raise m.WaterError()
except m.WaterError as e:
    print('WaterError default msg:', str(e) != '')

# Custom messages
try:
    raise m.PlantError('custom plant msg')
except m.PlantError as e:
    print('PlantError custom msg:', 'custom plant msg' in str(e))

# Catching PlantError as GardenError
try:
    raise m.PlantError('test')
except m.GardenError:
    print('PlantError caught as GardenError: True')
except Exception:
    print('PlantError caught as GardenError: False')

# Catching WaterError as GardenError
try:
    raise m.WaterError('test')
except m.GardenError:
    print('WaterError caught as GardenError: True')
except Exception:
    print('WaterError caught as GardenError: False')
" 2>&1)

    echo "$result" | grep -q "GardenError->Exception: True"         && ok "GardenError inherits from Exception"    || ko "GardenError must inherit from Exception"
    echo "$result" | grep -q "PlantError->GardenError: True"        && ok "PlantError inherits from GardenError"   || ko "PlantError must inherit from GardenError"
    echo "$result" | grep -q "WaterError->GardenError: True"        && ok "WaterError inherits from GardenError"   || ko "WaterError must inherit from GardenError"
    echo "$result" | grep -q "PlantError default msg: True"         && ok "PlantError has default message"         || ko "PlantError must have default error message"
    echo "$result" | grep -q "WaterError default msg: True"         && ok "WaterError has default message"         || ko "WaterError must have default error message"
    echo "$result" | grep -q "PlantError custom msg: True"          && ok "PlantError accepts custom message"      || ko "PlantError should accept custom message"
    echo "$result" | grep -q "PlantError caught as GardenError: True" && ok "PlantError catchable as GardenError" || ko "catching GardenError must catch PlantError"
    echo "$result" | grep -q "WaterError caught as GardenError: True" && ok "WaterError catchable as GardenError" || ko "catching GardenError must catch WaterError"

    # Output checks
    check_output "PlantError shown in output"   "$OUT" "PlantError"
    check_output "WaterError shown in output"   "$OUT" "WaterError"
    check_output "GardenError catches all"      "$OUT" "GardenError"
    check_output "program completes"            "$OUT" "All custom|correctly|work"
fi

# ═══════════════════════════════════════════════════════════════
hdr "EX4 — ft_finally_block.py"
# ═══════════════════════════════════════════════════════════════

if [ -f "$EX4" ]; then
    OUT=$(run_py "$EX4")

    check_flake8 "$EX4"
    check_mypy "$EX4"
    check_type_hints "$EX4"
    check_no_crash "program runs without crash" "$EX4"

    if grep -qE "finally\s*:" "$EX4"; then
        ok "uses finally block"
    else
        ko "no finally block found — REQUIRED"
    fi

    if grep -qE "try\s*:" "$EX4" && grep -qE "except" "$EX4"; then
        ok "uses try/except"
    else
        ko "no try/except found"
    fi

    if grep -qE "def water_plant" "$EX4"; then
        ok "function water_plant() defined"
    else
        ko "function water_plant() missing"
    fi

    if grep -qE "def test_watering_system" "$EX4"; then
        ok "function test_watering_system() defined"
    else
        ko "function test_watering_system() missing"
    fi

    if grep -qE "capitalize\(\)" "$EX4"; then
        ok "uses str.capitalize() to check plant name"
    else
        ko "must use capitalize() to validate plant name"
    fi

    # Output checks — valid run
    check_output "Opening watering system printed"      "$OUT" "Opening watering system"
    check_output "Watering Tomato succeeds"             "$OUT" "Watering Tomato.*OK|Tomato.*\[OK\]"
    check_output "Watering Lettuce succeeds (valid run)" "$OUT" "Watering Lettuce.*OK|Lettuce.*\[OK\]"
    check_output "Watering Carrots succeeds"            "$OUT" "Watering Carrots.*OK|Carrots.*\[OK\]"
    check_output "Closing watering system (valid run)"  "$OUT" "Closing watering system"
    check_output "PlantError caught for 'lettuce'"      "$OUT" "PlantError.*lettuce|lettuce.*PlantError|Caught PlantError"
    check_output "cleanup always happens message"       "$OUT" "Cleanup always happens|always happens"

    # Finally always runs — even with error
    CLOSE_COUNT=$(echo "$OUT" | grep -c "Closing watering system")
    if [ "$CLOSE_COUNT" -ge 2 ]; then
        ok "finally runs twice (once per test_watering_system call)"
    elif [ "$CLOSE_COUNT" -eq 1 ]; then
        wa "only 1 'Closing watering system' — expected 2 (one per call)"
    else
        ko "'Closing watering system' never printed — finally not working"
    fi

    # water_plant logic via import
    result=$(python3 -c "
import importlib.util
spec = importlib.util.spec_from_file_location('m', '$EX4')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# Valid (capitalized)
try:
    m.water_plant('Tomato')
    print('Tomato:OK')
except Exception as e:
    print('Tomato:RAISED:', e)

# Invalid (lowercase)
try:
    m.water_plant('tomato')
    print('tomato:NO_RAISE')
except Exception as e:
    print('tomato:RAISED:', type(e).__name__)

# Already capitalized edge case
try:
    m.water_plant('Rose')
    print('Rose:OK')
except Exception:
    print('Rose:RAISED')
" 2>&1)

    echo "$result" | grep -q "Tomato:OK"      && ok "water_plant('Tomato') succeeds"          || ko "water_plant('Tomato') should succeed"
    echo "$result" | grep -q "tomato:RAISED:" && ok "water_plant('tomato') raises exception"   || ko "water_plant('tomato') should raise"
    echo "$result" | grep -q "Rose:OK"        && ok "water_plant('Rose') succeeds"             || ko "water_plant('Rose') should succeed"
fi

# ═══════════════════════════════════════════════════════════════
hdr "GENERAL — Python version, no crashes, no globals"
# ═══════════════════════════════════════════════════════════════

PY_VER=$(python3 --version 2>&1 | grep -oE "[0-9]+\.[0-9]+")
PY_MAJOR=$(echo "$PY_VER" | cut -d. -f1)
PY_MINOR=$(echo "$PY_VER" | cut -d. -f2)
if [ "$PY_MAJOR" -ge 3 ] && [ "$PY_MINOR" -ge 10 ]; then
    ok "Python $PY_VER >= 3.10"
else
    ko "Python $PY_VER < 3.10 — subject requires 3.10+"
fi

for f in "$EX0" "$EX1" "$EX2" "$EX3" "$EX4"; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    # Check for global variables
    out=$(python3 -c "
import ast
with open('$f') as fh:
    tree = ast.parse(fh.read())
globals_found = []
for node in tree.body:
    if isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name) and not t.id.startswith('_'):
                globals_found.append(t.id)
if globals_found:
    print('GLOBAL:', ', '.join(globals_found))
else:
    print('OK')
" 2>&1)
    if echo "$out" | grep -q "^OK"; then
        ok "$base: no global variables"
    else
        wa "$base: possible globals found: $out"
    fi
done

# ═══════════════════════════════════════════════════════════════
hdr "EVALUATION SHEET — Key questions to ask"
# ═══════════════════════════════════════════════════════════════

echo ""
echo -e "${YELLOW}  These are questions from the evaluation sheet — verify manually:${RESET}"
echo ""
echo -e "  ${BOLD}EX0:${RESET}"
echo "  → Why use try/except instead of an if/else to check int()?"
echo "  → What exception does int('abc') raise? (ValueError)"
echo "  → Does your program keep running after the error? How?"
echo ""
echo -e "  ${BOLD}EX1:${RESET}"
echo "  → What is 'raise' and when do you use it?"
echo "  → What's the difference between catching and raising an exception?"
echo "  → Can you raise a ValueError vs a generic Exception? What's the difference?"
echo ""
echo -e "  ${BOLD}EX2:${RESET}"
echo "  → Why does Python have different error types?"
echo "  → How do you catch multiple types in one except line?"
echo "  → What does 'except (ValueError, TypeError) as e:' do?"
echo ""
echo -e "  ${BOLD}EX3:${RESET}"
echo "  → When should you create custom exceptions instead of using built-in ones?"
echo "  → Why does PlantError inherit from GardenError instead of Exception?"
echo "  → How does inheritance help organize errors?"
echo ""
echo -e "  ${BOLD}EX4:${RESET}"
echo "  → When does the finally block run? Always? Even after return?"
echo "  → Why is resource cleanup important even when errors happen?"
echo "  → What happens if you put the cleanup INSIDE the try block?"

# ═══════════════════════════════════════════════════════════════
hdr "SUMMARY"
# ═══════════════════════════════════════════════════════════════

total=$((pass + fail))
echo ""
echo -e "  Total:    $total"
echo -e "  ${GREEN}Passed:   $pass${RESET}"
[ "$fail" -gt 0 ] && echo -e "  ${RED}Failed:   $fail${RESET}" || echo "  Failed:   0"
[ "$warn" -gt 0 ] && echo -e "  ${YELLOW}Warnings: $warn${RESET}"
echo ""

if [ "$fail" -eq 0 ]; then
    echo -e "${BOLD}${GREEN}  ✓ All tests passed!${RESET}"
else
    echo -e "${BOLD}${RED}  ✗ Some tests failed — see above${RESET}"
fi
echo ""
