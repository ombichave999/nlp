import json
import os

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <script>
    if (window.location.hostname !== 'examhack-py.vercel.app') {
      window.location.replace('https://examhack-py.vercel.app' + window.location.search + window.location.hash);
    }
  </script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IDLE Shell 3.14.6</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    html, body {
      width: 100%;
      height: 100%;
      background: #ffffff;
      color: #000000;
      font-family: "Courier New", Courier, monospace;
      font-size: 13.5px;
      line-height: 1.42;
      overflow-x: hidden;
    }

    /* Windows 10/11 Classic Titlebar - NO macOS buttons, NO card frame */
    .idle-titlebar {
      background: #f1f3f4;
      border-bottom: 1px solid #d0d0d0;
      height: 30px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 4px 0 8px;
      font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, Tahoma, sans-serif;
      font-size: 12px;
      color: #202124;
      user-select: none;
    }
    .idle-title-left {
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 400;
    }
    .py-icon {
      font-size: 14px;
    }

    /* Windows Style Minimize / Maximize / Close Buttons */
    .win-controls {
      display: flex;
      height: 100%;
    }
    .win-btn {
      width: 44px;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      color: #444;
      cursor: pointer;
      font-family: "Segoe UI Symbol", "Segoe UI", sans-serif;
    }
    .win-btn:hover {
      background: #e5e5e5;
    }
    .win-btn.close:hover {
      background: #e81123;
      color: #ffffff;
    }

    /* Classic IDLE Menu Bar */
    .idle-menubar {
      background: #f9f9f9;
      border-bottom: 1px solid #e1e1e1;
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 3px 12px;
      font-family: "Segoe UI", Tahoma, sans-serif;
      font-size: 12px;
      color: #222;
      user-select: none;
    }
    .idle-menubar span {
      cursor: pointer;
      padding: 1px 4px;
    }
    .idle-menubar span:hover {
      background: #e5f1fb;
      outline: 1px solid #70c0e7;
    }

    /* Subject Switcher Toolbar */
    .subject-toolbar {
      background: #f1f3f4;
      border-bottom: 1px solid #d5d5d5;
      padding: 6px 12px;
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: "Segoe UI", Tahoma, sans-serif;
      font-size: 12px;
      flex-wrap: wrap;
    }
    .toolbar-label {
      font-weight: 600;
      color: #333;
    }
    .subject-btn {
      background: #ffffff;
      border: 1px solid #b0b0b0;
      padding: 4px 12px;
      font-size: 12px;
      font-family: inherit;
      cursor: pointer;
      border-radius: 2px;
      color: #111;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 500;
      transition: all 0.15s;
    }
    .subject-btn:hover {
      background: #e9f3ff;
      border-color: #0066cc;
    }
    .subject-btn.active {
      background: #0066cc;
      color: #ffffff;
      border-color: #004c99;
      font-weight: bold;
    }

    /* Main IDLE Shell Body */
    .idle-shell-body {
      padding: 10px 14px 40px 14px;
      background: #ffffff;
      min-height: calc(100vh - 80px);
    }

    .shell-intro {
      color: #000000;
      margin-bottom: 12px;
      white-space: pre-wrap;
    }
    .shell-intro .comment-line {
      color: #dd0000;
    }

    /* Interactive Command Prompt Line */
    .prompt-box {
      margin: 10px 0 16px 0;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .prompt-line {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 14px;
    }
    .prompt-arrow {
      color: #770000;
      font-weight: bold;
      font-size: 14px;
      user-select: none;
    }
    .prompt-input {
      flex: 1;
      font-family: "Courier New", Courier, monospace;
      font-size: 13.5px;
      border: 1px solid #777777;
      padding: 4px 8px;
      outline: none;
      background: #ffffff;
      color: #000000;
    }
    .prompt-input:focus {
      border-color: #0000ff;
      box-shadow: 0 0 2px #0000ff;
    }

    /* Sub-filters / Quick Tags */
    .filter-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
      align-items: center;
      font-size: 11.5px;
      font-family: "Segoe UI", Tahoma, sans-serif;
      margin-top: 2px;
    }
    .tag-chip {
      background: #f0f0f0;
      border: 1px solid #c0c0c0;
      padding: 2px 7px;
      cursor: pointer;
      border-radius: 2px;
      color: #333;
    }
    .tag-chip:hover, .tag-chip.active {
      background: #333333;
      color: #ffffff;
      border-color: #111111;
    }

    /* Restart Line (Exact IDLE style: ============ RESTART ============) */
    .restart-bar {
      color: #0000ff;
      font-weight: bold;
      font-size: 13px;
      margin: 22px 0 6px 0;
      display: flex;
      align-items: center;
      gap: 8px;
      user-select: none;
    }
    .restart-bar::before, .restart-bar::after {
      content: "==================================================";
      letter-spacing: -2px;
      flex: 1;
      overflow: hidden;
      white-space: nowrap;
    }

    /* Practical Code Block */
    .practical-item {
      margin-bottom: 24px;
      border-bottom: 1px dotted #ccc;
      padding-bottom: 16px;
    }
    .practical-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }
    .practical-title {
      font-weight: bold;
      color: #000000;
      font-size: 13.5px;
    }
    .copy-btn {
      font-family: "Segoe UI", Tahoma, sans-serif;
      font-size: 11px;
      padding: 2px 8px;
      background: #e1e1e1;
      border: 1px solid #adadad;
      border-radius: 2px;
      cursor: pointer;
      color: #222;
    }
    .copy-btn:hover {
      background: #d0d0d0;
    }
    .copy-btn.copied {
      background: #008000;
      color: #ffffff;
      border-color: #006000;
    }

    pre.code-block {
      background: transparent;
      color: #000000;
      font-family: "Courier New", Courier, monospace;
      font-size: 13.5px;
      line-height: 1.42;
      white-space: pre-wrap;
      word-break: break-all;
    }

    /* Syntax Highlighting in IDLE Style */
    .py-kw { color: #ff7700; font-weight: bold; }
    .py-str { color: #00aa00; }
    .py-comment { color: #dd0000; }
    .py-builtin { color: #900090; }
    .py-def { color: #0000ff; font-weight: bold; }

    /* Expected Output in IDLE Blue */
    .output-box {
      margin-top: 6px;
      color: #0000ff;
      white-space: pre-wrap;
    }

    #no-results {
      color: #dd0000;
      padding: 18px 0;
      display: none;
    }
  </style>
</head>
<body>

  <!-- Windows Classic Titlebar -->
  <div class="idle-titlebar">
    <div class="idle-title-left">
      <span class="py-icon">🐍</span>
      <span>*IDLE Shell 3.14.6*</span>
    </div>
    <div class="win-controls">
      <div class="win-btn" title="Minimize">—</div>
      <div class="win-btn" title="Maximize">▢</div>
      <div class="win-btn close" title="Close">✕</div>
    </div>
  </div>

  <!-- Classic Menu Bar -->
  <div class="idle-menubar">
    <span>File</span>
    <span>Edit</span>
    <span>Shell</span>
    <span>Debug</span>
    <span>Options</span>
    <span>Window</span>
    <span>Help</span>
  </div>

  <!-- Subject Switcher Toolbar -->
  <div class="subject-toolbar">
    <span class="toolbar-label">Subject:</span>
    <button class="subject-btn active" id="btn-crypto" onclick="switchSubject('crypto')">
      🔐 Cryptography &amp; Security Practicals (1-12)
    </button>
    <button class="subject-btn" id="btn-sma" onclick="switchSubject('sma')">
      📊 Social Media Analytics (SMA Units 1-3)
    </button>
  </div>

  <!-- Main IDLE Shell Body -->
  <div class="idle-shell-body">
    <div class="shell-intro">Python 3.14.6 (tags/v3.14.6:cf84c8a, Oct 13 2026, 09:30:00) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
<span class="comment-line"># [SYSTEM]: Session initialized. Use the interactive prompt below to search or filter codes.</span></div>

    <!-- Interactive Search / Filter Prompt -->
    <div class="prompt-box">
      <div class="prompt-line">
        <span class="prompt-arrow">&gt;&gt;&gt;</span>
        <input type="text" id="shell-search" class="prompt-input" placeholder="Type search keyword (e.g. aes, rsa, nmap, firewall, unit 1, layer)..." oninput="filterPracticals()">
      </div>
      <!-- Tags for Crypto -->
      <div class="filter-tags" id="tags-crypto">
        <span style="color:#666; font-size:11px;">Quick Jump:</span>
        <span class="tag-chip active" onclick="setChip(this, '')">All (12)</span>
        <span class="tag-chip" onclick="setChip(this, 'AES')">AES</span>
        <span class="tag-chip" onclick="setChip(this, 'DES')">DES</span>
        <span class="tag-chip" onclick="setChip(this, 'RSA')">RSA</span>
        <span class="tag-chip" onclick="setChip(this, 'Signature')">Digital Signature</span>
        <span class="tag-chip" onclick="setChip(this, 'MD5')">MD5</span>
        <span class="tag-chip" onclick="setChip(this, 'SHA')">SHA-1</span>
        <span class="tag-chip" onclick="setChip(this, 'MAC')">MAC</span>
        <span class="tag-chip" onclick="setChip(this, 'Tampering')">Tampering</span>
        <span class="tag-chip" onclick="setChip(this, 'ECDH')">ECDH</span>
        <span class="tag-chip" onclick="setChip(this, 'Firewall')">Firewall</span>
        <span class="tag-chip" onclick="setChip(this, 'Nmap')">Nmap</span>
        <span class="tag-chip" onclick="setChip(this, 'Theory')">Theory</span>
      </div>
      <!-- Tags for SMA -->
      <div class="filter-tags" id="tags-sma" style="display:none;">
        <span style="color:#666; font-size:11px;">Quick Jump:</span>
        <span class="tag-chip active" onclick="setChip(this, '')">All Units</span>
        <span class="tag-chip" onclick="setChip(this, 'Unit 1')">Unit 1 (Layers & Cycle)</span>
        <span class="tag-chip" onclick="setChip(this, 'Unit 2')">Unit 2 (Network & Search)</span>
        <span class="tag-chip" onclick="setChip(this, 'Unit 3')">Unit 3 (Tools & Analytics)</span>
        <span class="tag-chip" onclick="setChip(this, 'Quick Reference')">Exam Quick Reference</span>
      </div>
    </div>

    <!-- Cryptography Section -->
    <div id="section-crypto">
      __CRYPTO_ITEMS__
    </div>

    <!-- SMA Section -->
    <div id="section-sma" style="display:none;">
      __SMA_ITEMS__
    </div>

    <div id="no-results">
      Traceback (most recent call last):<br>
      &nbsp;&nbsp;File "&lt;stdin&gt;", line 1, in &lt;module&gt;<br>
      NameError: name '<span id="missing-query"></span>' is not defined. No practical or question found matching query.
    </div>

  </div>

  <script>
    let currentSubject = 'crypto';
    let currentChip = '';

    function switchSubject(subject) {
      currentSubject = subject;
      const btnCrypto = document.getElementById('btn-crypto');
      const btnSma = document.getElementById('btn-sma');
      const secCrypto = document.getElementById('section-crypto');
      const secSma = document.getElementById('section-sma');
      const tagsCrypto = document.getElementById('tags-crypto');
      const tagsSma = document.getElementById('tags-sma');

      if (subject === 'crypto') {
        btnCrypto.classList.add('active');
        btnSma.classList.remove('active');
        secCrypto.style.display = 'block';
        secSma.style.display = 'none';
        tagsCrypto.style.display = 'flex';
        tagsSma.style.display = 'none';
      } else {
        btnSma.classList.add('active');
        btnCrypto.classList.remove('active');
        secSma.style.display = 'block';
        secCrypto.style.display = 'none';
        tagsSma.style.display = 'flex';
        tagsCrypto.style.display = 'none';
      }
      currentChip = '';
      resetChips();
      filterPracticals();
    }

    function resetChips() {
      const activeChips = document.querySelectorAll('.filter-tags .tag-chip');
      activeChips.forEach(chip => {
        if (chip.textContent.includes('All')) chip.classList.add('active');
        else chip.classList.remove('active');
      });
    }

    function setChip(el, keyword) {
      const parent = el.parentElement;
      parent.querySelectorAll('.tag-chip').forEach(c => c.classList.remove('active'));
      el.classList.add('active');
      currentChip = keyword.toLowerCase();
      filterPracticals();
    }

    function filterPracticals() {
      const searchVal = document.getElementById('shell-search').value.toLowerCase().trim();
      const activeSection = currentSubject === 'crypto' ? document.getElementById('section-crypto') : document.getElementById('section-sma');
      const items = activeSection.querySelectorAll('.practical-item');
      let visibleCount = 0;

      items.forEach(item => {
        const text = item.innerText.toLowerCase();
        const matchesSearch = !searchVal || text.includes(searchVal);
        const matchesChip = !currentChip || text.includes(currentChip);

        if (matchesSearch && matchesChip) {
          item.style.display = 'block';
          visibleCount++;
        } else {
          item.style.display = 'none';
        }
      });

      const noRes = document.getElementById('no-results');
      if (visibleCount === 0) {
        document.getElementById('missing-query').innerText = searchVal || currentChip;
        noRes.style.display = 'block';
      } else {
        noRes.style.display = 'none';
      }
    }

    function copySnippet(id, btn) {
      const el = document.getElementById(id);
      const text = el.innerText;
      navigator.clipboard.writeText(text).then(() => {
        const originalText = btn.innerText;
        btn.innerText = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => {
          btn.innerText = originalText;
          btn.classList.remove('copied');
        }, 1800);
      });
    }
  </script>
</body>
</html>
"""

crypto_practicals = [
    {
        "id": "crypto-1",
        "title": "Practical 1: Symmetric Encryption & Decryption using AES (Advanced Encryption Standard)",
        "file": "AES.py",
        "code": """from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(key, text):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(text.encode(), AES.block_size))

def aes_decrypt(key, cipher_text):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(cipher_text), AES.block_size).decode()

key = b"mysecretkey12345"
text = "Everyone"

cipher_text = aes_encrypt(key, text)
print("Cipher (hex):", cipher_text.hex())

plain_text = aes_decrypt(key, cipher_text)
print("Plain Text:", plain_text)""",
        "output": """>>> ================================ RESTART: AES.py ================================
Cipher (hex): 4e4b6c311c9fdf196d22efdfa7e4466d
Plain Text: Everyone"""
    },
    {
        "id": "crypto-2",
        "title": "Practical 2: Symmetric Encryption & Decryption using DES (Data Encryption Standard)",
        "file": "DES.py",
        "code": """from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(key, text):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text.encode(), DES.block_size)
    return cipher.encrypt(padded_text)

def des_decrypt(key, cipher_text):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(cipher_text)
    return unpad(decrypted_text, DES.block_size).decode()

key = b"mynewkey"
text = "Everyone"

cipher_text = des_encrypt(key, text)
print("Encrypted Text:", cipher_text)

plain_text = des_decrypt(key, cipher_text)
print("Decrypted Text:", plain_text)""",
        "output": """>>> ================================ RESTART: DES.py ================================
Encrypted Text: b'\\x97\\xe3b\\xf1\\xb0\\xc7\\xc0\\xda\\x83\\xd8\\x84\\x98\\x13\\xf2\\x04\\xae'
Decrypted Text: Everyone"""
    },
    {
        "id": "crypto-3",
        "title": "Practical 3: Asymmetric Encryption & Decryption using RSA",
        "file": "Rivest-Shamir-Adleman.py",
        "code": """from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

priv = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

pub = priv.public_key()

pad = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
)

msg = b"My social security number"

cipher = pub.encrypt(msg, pad)
print("Ciphertext:", cipher[:20], "...")

decrypted = priv.decrypt(cipher, pad)
print("Decrypted:", decrypted)
print("Decrypted:", decrypted.decode("utf-8"))""",
        "output": """>>> ================================ RESTART: RSA.py ================================
Ciphertext: b'\\x17\\xceM\\xef(\\xb9\\x9eg\\x8c\"\\x14\\r}f\\xf8b\\xa8x\\x16\\x13' ...
Decrypted: b'My social security number'
Decrypted: My social security number"""
    },
    {
        "id": "crypto-4",
        "title": "Practical 4: Digital Signature Creation & Verification using RSA",
        "file": "Data Signature Implementation.py",
        "code": """import rsa

public_key, private_key = rsa.newkeys(512)

message = 'Data Security Practical'

signature = rsa.sign(message.encode(), private_key, 'SHA-256')
print("Digital Signature Created")

try:
    rsa.verify(message.encode(), signature, public_key)
    print("The signature is valid.")
except rsa.VerificationError:
    print("The signature is not valid.")""",
        "output": """>>> ================================ RESTART: Data_Signature.py ================================
Digital Signature Created
The signature is valid."""
    },
    {
        "id": "crypto-5",
        "title": "Practical 5: Hashing using MD5 (Message Digest Algorithm 5)",
        "file": "MD5.py",
        "code": """import hashlib

message = "Hlo, World"

hashed_message = hashlib.md5(message.encode())

print(hashed_message.hexdigest())""",
        "output": """>>> ================================ RESTART: MD5.py ================================
423c4386723da360690f5d6a35054083"""
    },
    {
        "id": "crypto-6",
        "title": "Practical 6: Hashing using SHA-1 (Secure Hash Algorithm 1)",
        "file": "SHA-1.py",
        "code": """import hashlib

text = input("Enter the value to encode: ")

result = hashlib.sha1(text.encode())

print("The hexadecimal equivalent of SHA is", result.hexdigest())""",
        "output": """>>> ================================ RESTART: SHA1.py ================================
Enter the value to encode: test
The hexadecimal equivalent of SHA is a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"""
    },
    {
        "id": "crypto-7",
        "title": "Practical 7: Message Authentication Code (MAC) using HMAC",
        "file": "Message Authentication Code (MAC).py",
        "code": """import hmac
import hashlib

key = b"secret-key"

msg_sent = b"Transfer $100 to Alice"
mac1 = hmac.new(key, msg_sent, hashlib.sha256).hexdigest()
print(mac1)

msg_received = b"Transfer $100 to Bob"
mac2 = hmac.new(key, msg_received, hashlib.sha256).hexdigest()
print(mac2)

is_valid = hmac.compare_digest(mac1, mac2)
print(is_valid)""",
        "output": """>>> ================================ RESTART: MAC.py ================================
95b79e8f18e264973861dd02999fa7524c53bc15e0d5680815ad4f92cc4ee69e
f0e7c55485e84de6b8c9bcaf37ad98f3093f5756aeb15b6c2a3134556928a6bd
False"""
    },
    {
        "id": "crypto-8",
        "title": "Practical 8: Data Tampering Detection using HMAC-SHA256",
        "file": "Data Tampering.py",
        "code": """import hmac
import hashlib

key = b"secret-key"

msg_sent = b"Transfer $100 to Alice"
mac1 = hmac.new(key, msg_sent, hashlib.sha256).hexdigest()
print(mac1)

tampered_msg = b"Transfer $9999 to Bob"
mac2 = hmac.new(key, tampered_msg, hashlib.sha256).hexdigest()
print(mac2)

is_valid = hmac.compare_digest(mac1, mac2)
is_tampered = not is_valid
print(is_tampered)""",
        "output": """>>> ================================ RESTART: Tampering.py ================================
95b79e8f18e264973861dd02999fa7524c53bc15e0d5680815ad4f92cc4ee69e
80cb38085f7123529f1eddecee3a3dddc6578da3fd00246fde354915440538c6
True"""
    },
    {
        "id": "crypto-9",
        "title": "Practical 9: Elliptic Curve Diffie-Hellman (ECDH) Key Exchange",
        "file": "ECDH.py",
        "code": """from cryptography.hazmat.primitives.asymmetric import ec

a_priv = ec.generate_private_key(ec.SECP256R1())
b_priv = ec.generate_private_key(ec.SECP256R1())

a_secret = a_priv.exchange(
    ec.ECDH(),
    b_priv.public_key()
)

b_secret = b_priv.exchange(
    ec.ECDH(),
    a_priv.public_key()
)

print("Keys Match?", a_secret == b_secret)""",
        "output": """>>> ================================ RESTART: ECDH.py ================================
Keys Match? True"""
    },
    {
        "id": "crypto-10",
        "title": "Practical 10: Intercepted Key Exchange (Tampering Demonstration)",
        "file": "Tampered or Intercepted Exchange.py",
        "code": """from cryptography.hazmat.primitives.asymmetric import ec

a_priv = ec.generate_private_key(ec.SECP256R1())
b_priv = ec.generate_private_key(ec.SECP256R1())
hacker_priv = ec.generate_private_key(ec.SECP256R1())

intercepted_pub_key = hacker_priv.public_key()

a_secret = a_priv.exchange(
    ec.ECDH(),
    b_priv.public_key()
)

b_secret = b_priv.exchange(
    ec.ECDH(),
    a_priv.public_key()
)

print("Do the shared keys match? :", a_secret == b_secret)""",
        "output": """>>> ================================ RESTART: Intercepted_Exchange.py ================================
Do the shared keys match? : True"""
    },
    {
        "id": "crypto-11",
        "title": "Practical 11: Demonstration of Firewall Configuration Using Windows Defender Firewall",
        "file": "Windows Defender Firewall Guide",
        "code": """# AIM: Demonstration of Firewall Configuration Using Windows Defender Firewall
# Follow these 12 practical steps:

Step 1: Press Windows + R to open the Run prompt.
Step 2: Type: "control firewall.cpl" and click OK.
Step 3: Click on "Advanced Settings" in the left sidebar.
Step 4: Select "Outbound Rules" (or "Inbound Rules").
Step 5: In the right Actions panel, click "New Rule...".
Step 6: Choose "Program" and click Next.
Step 7: Browse and select the application executable path:
        Example: "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        (or Google Chrome application path), then click Next.
Step 8: Select "Block the connection" and click Next.
Step 9: Keep all network profiles selected (Domain, Private, Public) and click Next.
Step 10: Name the rule (e.g. "Block Microsoft Edge" or "Block Chrome") and click Finish.
Step 11: Verification: Launch the blocked browser and attempt to browse any site. Traffic will be blocked!
Step 12: Cleanup: In Outbound Rules, right-click the rule -> "Disable Rule" or "Delete" to restore access.""",
        "output": """>>> ================================ LAB DEMO: Windows Defender Firewall ================================
Status: Outbound rule configured successfully.
Connection state: Blocked for targeted application."""
    },
    {
        "id": "crypto-12",
        "title": "Practical 12: Vulnerability Scanning Using Nmap on Windows",
        "file": "Nmap Vulnerability Scanning Guide",
        "code": """# AIM: Vulnerability Scanning and Port Scanning Using Nmap on Windows
# Step-by-Step Commands:

Step 1: Download & Install Nmap Installer from official website: https://nmap.org
        Ensure Npcap is checked during setup.

Step 2: Verify Nmap Installation in Command Prompt:
        nmap --version
        
Step 3: Scan Your Own Computer (Loopback):
        nmap localhost
        # Alternatively:
        nmap 127.0.0.1
        
Step 4: Find Local IP Address:
        ipconfig
        # Note the IPv4 Address (e.g., 192.168.1.15)
        
Step 5: Scan the Local IP Address:
        nmap 192.168.1.15

# Additional Common Scanning Techniques:
nmap -sS 192.168.1.15    # SYN Stealth Scan
nmap -sV 192.168.1.15    # Version / Service Detection
nmap -O  192.168.1.15    # Operating System Detection
nmap -A  192.168.1.15    # Aggressive Scan (OS, Version, Scripting, Traceroute)""",
        "output": """>>> ================================ LAB DEMO: Nmap Scanner ================================
Starting Nmap 7.9X ( https://nmap.org )
Nmap scan report for localhost (127.0.0.1)
PORT    STATE SERVICE
135/tcp open  msrpc
445/tcp open  microsoft-ds
Nmap done: 1 IP address (1 host up) scanned."""
    },
    {
        "id": "crypto-13",
        "title": "Reference: Cryptography Aim & Background Theory Notes",
        "file": "AIM_and_THEORY.pdf",
        "code": """\"\"\"
CRYPTOGRAPHY PRACTICALS - BACKGROUND THEORY REFERENCE
======================================================
1. Symmetric Encryption:
   - Same key used for both encryption and decryption.
   - Fast, efficient, and used for sensitive data storage & transmission.
   - DES: Block cipher encrypting in 64-bit blocks with 56-bit effective key.
   - AES: Global standard, 128-bit blocks, supports 128, 192, and 256-bit keys.

2. Asymmetric Cryptography (Public-Key Cryptography):
   - Uses mathematically related key pairs: Public Key (shared) & Private Key (secret).
   - RSA (Rivest-Shamir-Adleman): Factoring large primes for encryption/decryption.
   - ECDH (Elliptic Curve Diffie-Hellman): Establishes shared secret over insecure channel.

3. Hashing and Integrity:
   - One-way mathematical function producing a fixed-length digest. Cannot reverse.
   - MD5: Generates 128-bit hash (32 hex characters).
   - SHA-1: Generates 160-bit hash (40 hex characters).

4. MAC (Message Authentication Code):
   - Verifies authenticity and integrity using secret key + message + HMAC algorithm.

5. Digital Signatures:
   - Provides Authenticity, Integrity, and Non-Repudiation.
   - Sender signs with Private Key; anyone verifies with Sender's Public Key.
\"\"\"""",
        "output": """>>> ================================ THEORY REFERENCE ================================
Summary loaded. Review docstring above for complete 6-mark theory answers."""
    }
]

sma_items = [
    {
        "id": "sma-1",
        "title": "Unit 1 - Q1: Characteristics and Types of Social Media Analytics (SMA)",
        "file": "Unit 1 - Q1",
        "code": """\"\"\"
Social Media Analytics (SMA) is the process of collecting and analysing social media
data to understand users, trends and performance, and to support decisions.

Characteristics of Social Media used in SMA:
1. User-generated content: Posts, photos, videos, blogs and reviews.
2. Interactivity: Likes, comments, shares, reactions.
3. Connectivity: Connects people across geographical boundaries.
4. Real-time communication: Instant information and feedback.
5. Multimedia sharing: Text, images, videos, audio, live streams.
6. Data generation: Constant streams of trackable data points.
7. Viral nature & global reach: Content can spread quickly worldwide.

Types of Social Media Analytics:
- Sentiment Analytics: Identifies positive, negative or neutral opinions.
- Text Analytics: Extracts keywords and insights from posts/comments.
- Network Analytics: Studies relationships and influence among users.
- Competitive Analytics: Compares organization against competitors.
- Influencer Analytics: Measures influencer reach and ROI.
- Action/Engagement Analytics: Measures likes, shares, clicks, views.
\"\"\"""",
        "output": """>>> ================================ UNIT 1: Q1 ANSWER ================================
Characteristics & Types of SMA verified and loaded."""
    },
    {
        "id": "sma-2",
        "title": "Unit 1 - Q2: SMA in Small Organization vs Large Organization",
        "file": "Unit 1 - Q2",
        "code": """\"\"\"
Small Organizations:
1. Budget & Scale: Limited budget, small workforce, local/regional focus.
2. Objectives: Increase local brand awareness, build relationships, customer service.
3. Metrics: Likes, comments, shares, reach, reviews.
4. Tools: Meta Business Suite, basic built-in analytics dashboards.
5. Action: Direct personal replies to customer feedback.
6. Challenges: Limited staff, time, budget and analytics skills.

Large Organizations:
1. Budget & Scale: Global market, massive cross-platform data volume.
2. Objectives: Brand reputation, multi-region campaigns, crisis management, ROI.
3. Metrics: Brand sentiment, share of voice, conversion funnels.
4. Tools: Brandwatch, Talkwalker, Sprinklr, Meltwater.
5. Action: Cross-departmental business intelligence.
6. Challenges: Data silos, privacy compliance, tool costs.
\"\"\"""",
        "output": """>>> ================================ UNIT 1: Q2 ANSWER ================================
Small vs Large Organization comparison loaded."""
    },
    {
        "id": "sma-3",
        "title": "Unit 1 - Q3: Seven Layers of Social Media Analytics",
        "file": "Unit 1 - Q3",
        "code": """\"\"\"
The Seven Layers of Social Media Analytics:
1. Data Sources Layer:
   Platforms: Facebook, Instagram, X, LinkedIn, YouTube, blogs, review boards.
2. Data Collection Layer:
   Methods: APIs, web scraping, RSS feeds, monitoring tools.
3. Data Storage Layer:
   Storage: MySQL, MongoDB, HDFS, S3, Snowflake, BigQuery.
4. Data Processing Layer:
   Cleaning: Removing spam/duplicates, tokenization, stop-word removal.
5. Data Analysis Layer:
   Techniques: Sentiment analysis, text mining, network modeling, predictive analytics.
6. Data Visualization and Reporting Layer:
   Dashboards: Tableau, Power BI, charts, graphs, word clouds.
7. Decision and Business Intelligence Layer:
   Actionable insights for marketing, product improvements, customer support.
\"\"\"""",
        "output": """>>> ================================ UNIT 1: Q3 ANSWER ================================
Seven Layers architecture loaded."""
    },
    {
        "id": "sma-4",
        "title": "Unit 1 - Q4: The Social Media Analytics (SMA) Cycle",
        "file": "Unit 1 - Q4",
        "code": """\"\"\"
The Continuous 8-Step SMA Cycle:
1. Business Objective Definition: Define goal (e.g. brand awareness, lead gen).
2. Data Collection: Gather posts, comments, likes, shares, hashtags.
3. Data Preparation (Cleaning): Deduplicate, filter spam, normalize text.
4. Data Analysis: Sentiment analysis, network metrics, trend mining.
5. Visualization & Reporting: Generate graphs, charts, heat maps.
6. Decision Making: Allocate budget, select target demographics.
7. Implementation: Publish targeted campaigns, address complaints.
8. Monitoring & Feedback: Track CTR, conversions, sentiment, ROI; feed into next cycle.
\"\"\"""",
        "output": """>>> ================================ UNIT 1: Q4 ANSWER ================================
SMA Cycle steps loaded."""
    },
    {
        "id": "sma-5",
        "title": "Unit 2 - Q1: Nodes, Edges, and Ties with Example",
        "file": "Unit 2 - Q1",
        "code": """\"\"\"
Network = Nodes + Edges.
1. Nodes (Vertices):
   Entities such as people, organizations, social media accounts, or websites.
2. Edges (Links):
   Relationships such as following, friendship, messaging, mentions, sharing.
3. Tie:
   The nature and strength of connection between two nodes.
4. Directed Connection:
   Has direction (e.g. User A follows User B).
5. Undirected Connection:
   Mutual connection (e.g. mutual Facebook friends).
6. Tie Strength:
   Measured by interaction frequency, emotional intensity, or duration.

Example:
In a college network, students are Nodes. A line showing message exchange is an Edge.
Their communication relationship is the Tie.
\"\"\"""",
        "output": """>>> ================================ UNIT 2: Q1 ANSWER ================================
Nodes, Edges, and Ties loaded."""
    },
    {
        "id": "sma-6",
        "title": "Unit 2 - Q2: Degree, Distribution, Density, Trust, and Connectivity",
        "file": "Unit 2 - Q2",
        "code": """\"\"\"
Key Network Metrics:
1. Degree:
   The total number of edges connected to a node (In-degree + Out-degree).
2. Degree Distribution:
   Probability distribution showing how connections are spread across nodes.
3. Density:
   Ratio of actual existing edges to all possible edges: Density = E / (N * (N - 1)).
4. Trust:
   Degree of reliability and confidence between nodes through repeated interactions.
5. Connectivity:
   Whether nodes can reach one another through direct or indirect paths.
\"\"\"""",
        "output": """>>> ================================ UNIT 2: Q2 ANSWER ================================
Network metrics loaded."""
    },
    {
        "id": "sma-7",
        "title": "Unit 2 - Q3: Sources of Location Data & Categories of Location Analytics",
        "file": "Unit 2 - Q3",
        "code": """\"\"\"
Sources of Location Data:
1. GPS: Mobile device coordinates (latitude / longitude).
2. IP Address: Geolocation inferred from internet connection.
3. Social Media Check-ins & Geotags: User-tagged locations in posts.
4. Business Records: Customer addresses and physical billing regions.

Categories of Location Analytics:
1. Recommendations: Suggesting nearby stores, friends, or events.
2. Customer Segmentation: Segmenting users by city, state, or country.
3. Geo-Targeted Advertising: Displaying localized advertisements.
4. Spatial Heatmaps & Mapping: Visualizing geographic density of conversations.
5. Geo-Enrichment: Augmenting demographic data with geographic attributes.
\"\"\"""",
        "output": """>>> ================================ UNIT 2: Q3 ANSWER ================================
Location analytics loaded."""
    },
    {
        "id": "sma-8",
        "title": "Unit 2 - Q4 & Q5: Search Engine Tools & Search Engine Analytics Metrics",
        "file": "Unit 2 - Q4 & Q5",
        "code": """\"\"\"
Search Engine Tools:
1. Google Search Console: Query impressions, clicks, CTR, average position, indexing.
2. Google Analytics 4 (GA4): User traffic sources, session duration, conversions.
3. Bing Webmaster Tools: Search performance for Microsoft Bing.
4. SEO Tools (Ahrefs, Moz, SEMrush): Keyword research, backlink audits, competitor rankings.

Important Search Analytics Metrics:
- Impressions: Total times a snippet was shown in SERPs.
- Clicks: Total clicks on search result link.
- CTR (Click-Through Rate): (Clicks / Impressions) * 100.
- Average Position: Mean ranking in search results for a keyword.
- Organic Traffic: Non-paid search visitors.
- Conversion Rate: Percentage of search visitors completing goal.
\"\"\"""",
        "output": """>>> ================================ UNIT 2: Q4 & Q5 ANSWER ================================
Search Engine tools and metrics loaded."""
    },
    {
        "id": "sma-9",
        "title": "Unit 3 - Q1: Social Media Network Types",
        "file": "Unit 3 - Q1",
        "code": """\"\"\"
Network Types in Social Media:
1. Undirected Network:
   Reciprocal ties (e.g. Facebook friends).
2. Directed Network:
   One-way ties (e.g. Instagram / X followers).
3. Weighted Network:
   Edges carry numerical values representing frequency (e.g. number of messages sent).
4. Unweighted Network:
   Binary connection existence (connected vs not connected).
5. Bipartite (Two-Mode) Network:
   Two distinct node sets with edges only between them (e.g. Users connected to Hashtags).
6. Connected vs Disconnected Network:
   Connected has paths between every node; disconnected contains isolated groups.
\"\"\"""",
        "output": """>>> ================================ UNIT 3: Q1 ANSWER ================================
Network Types loaded."""
    },
    {
        "id": "sma-10",
        "title": "Unit 3 - Q2: Network Analytics Tools",
        "file": "Unit 3 - Q2",
        "code": """\"\"\"
Tools for Network Analysis:
1. Gephi:
   Open-source network analysis and visualization software; detects communities,
   calculates centrality, handles thousands of nodes.
2. NodeXL:
   Excel add-in; user-friendly social media data import, network metrics, graphs.
3. UCINET:
   Social network analysis package for matrix operations and centrality calculations.
4. Pajek:
   Specialized program for analysis and visualization of very large networks.
5. NetworkX:
   Python library for studying complex network structures and algorithms.
\"\"\"""",
        "output": """>>> ================================ UNIT 3: Q2 ANSWER ================================
Network Analytics tools loaded."""
    },
    {
        "id": "sma-11",
        "title": "Unit 3 - Q3 & Q4: Social Media Text Analytics & Action Analytics",
        "file": "Unit 3 - Q3 & Q4",
        "code": """\"\"\"
Text Analytics:
Extracts business value from unstructured user content (posts, comments, tweets).
- Steps: Noise removal & cleaning -> Tokenization -> Sentiment Analysis -> Topic Modeling.
- Value: Identifies customer dissatisfaction, emerging trends, brand perception.

Action Analytics:
Measures user actions and behaviors:
1. Engagement Actions: Likes, comments, reactions, shares, retweets.
2. Attention Measures: Impressions, reach, video watch duration.
3. Clicks: Outbound link clicks to landing pages.
4. Conversions: Form fills, downloads, purchases, sign-ups.
Tools: Meta Business Suite, Hootsuite, Sprout Social, Google Analytics 4.
\"\"\"""",
        "output": """>>> ================================ UNIT 3: Q3 & Q4 ANSWER ================================
Text and Action analytics loaded."""
    },
    {
        "id": "sma-12",
        "title": "Unit 3 - Q5 & Q6: Hyperlink Analytics & Network Visualization",
        "file": "Unit 3 - Q5 & Q6",
        "code": """\"\"\"
Hyperlink Analytics:
Extracts and analyzes URLs shared across social platforms:
1. In-links (Inbound): External links pointing into your website.
2. Out-links (Outbound): Links on your site sending users to external platforms.
3. Co-links: Two separate websites linking to the same third-party source.
Tools: Bitly (click tracking), GA4 (referrals), Ahrefs/Moz (backlink authority).

Network Visualization:
Graphical layout representing social network nodes and edges:
- Visual elements: Node color (community/group), Node size (centrality/influence),
  Edge thickness (weight/frequency).
- Key uses: Influencer discovery, community cluster identification, information cascade tracking.
\"\"\"""",
        "output": """>>> ================================ UNIT 3: Q5 & Q6 ANSWER ================================
Hyperlink Analytics and Visualization loaded."""
    },
    {
        "id": "sma-13",
        "title": "Complete SMA Exam Quick Reference Summary (Units 1, 2, 3)",
        "file": "Complete SMA Quick Reference",
        "code": """\"\"\"
SMA COMPLETE REVISION SHEET (6-MARK QUESTIONS)
==============================================
UNIT 1:
- SMA: Collecting, cleaning, analyzing social media data for business decision making.
- 7 Layers: Sources -> Collection -> Storage -> Processing -> Analysis -> Visualization -> Decision.
- SMA Cycle: Objective -> Collection -> Cleaning -> Analysis -> Visualization -> Decision -> Action -> Monitoring.

UNIT 2:
- Network: Nodes (Actors) + Edges (Relationships); Tie = Nature of connection.
- Metrics: Degree (connections), Density (actual/possible), Trust, Connectivity.
- Location: GPS, IP, Geotags; Used for Segmentation, Local Ads, Heatmaps.
- Search Metrics: Impressions, Clicks, CTR = (Clicks/Impressions)*100, Average Position.

UNIT 3:
- Network Types: Undirected, Directed, Weighted, Unweighted, Bipartite.
- Tools: Gephi, NodeXL, UCINET, Pajek, NetworkX.
- Text Analytics: Sentiment analysis, topic extraction from slang/emojis/text.
- Action Analytics: Engagement (likes/shares), Attention (reach), Clicks, Conversions.
- Hyperlinks: In-links, Out-links, Co-links; Referral attribution.
\"\"\"""",
        "output": """>>> ================================ COMPLETE SUMMARY ================================
All revision points loaded. Ready for exam!"""
    }
]

def render_items(items):
    out = []
    for item in items:
        escaped_code = item["code"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        escaped_out = item["output"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        block = f'''
      <div class="practical-item" id="{item["id"]}">
        <div class="practical-header">
          <div class="practical-title">{item["title"]}</div>
          <button class="copy-btn" onclick="copySnippet('code-{item["id"]}', this)">Copy Code</button>
        </div>
        <div class="restart-bar">{item["file"]}</div>
        <pre class="code-block" id="code-{item["id"]}">{escaped_code}</pre>
        <div class="output-box">{escaped_out}</div>
      </div>
'''
        out.append(block)
    return "\\n".join(out)

crypto_html = render_items(crypto_practicals)
sma_html = render_items(sma_items)

final_html = html_template.replace("__CRYPTO_ITEMS__", crypto_html).replace("__SMA_ITEMS__", sma_html)

nlp_dir = "/Users/om/.gemini/antigravity/scratch/nlp"
with open(os.path.join(nlp_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(final_html)

with open(os.path.join(nlp_dir, "examhack.py"), "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated index.html and examhack.py in nlp successfully!")
