<!DOCTYPE html>
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

    /* Main IDLE Shell Body - Edge-to-Edge Pure Canvas */
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
      justify-content: space-between;
      border-bottom: 1px solid #e0e0e0;
      padding-bottom: 4px;
      flex-wrap: wrap;
      gap: 6px;
    }
    .restart-text {
      color: #0000ff;
      letter-spacing: -0.2px;
    }
    .copy-btn {
      background: #f0f0f0;
      border: 1px solid #999999;
      color: #111111;
      font-family: "Segoe UI", Tahoma, sans-serif;
      font-size: 11px;
      padding: 2px 8px;
      cursor: pointer;
      border-radius: 2px;
    }
    .copy-btn:hover {
      background: #0000ff;
      color: #ffffff;
      border-color: #0000cc;
    }

    /* Aim text styled as IDLE Python Comment / Docstring */
    .aim-box {
      color: #770000;
      font-weight: bold;
      margin: 4px 0 8px 0;
      font-size: 13px;
    }

    /* IDLE Code Box (Pure text, authentic syntax colors) */
    .code-box {
      background: #ffffff;
      padding: 4px 0;
      white-space: pre-wrap;
      word-break: break-word;
      font-size: 13.5px;
      line-height: 1.42;
      color: #000000;
      user-select: text;
    }

    /* IDLE Syntax Highlighting */
    .kw { color: #ff7700; font-weight: bold; } /* Keywords */
    .builtin { color: #900090; } /* Builtin functions */
    .str { color: #00aa00; } /* Strings */
    .com { color: #dd0000; } /* Comments */

    /* Output Box (Exact IDLE Shell Blue) */
    .output-section {
      margin-top: 6px;
      padding-left: 0;
    }
    .output-label {
      color: #555555;
      font-size: 11px;
      font-family: "Segoe UI", Tahoma, sans-serif;
      text-transform: uppercase;
      margin-bottom: 2px;
    }
    .output-box {
      color: #0000ff; /* Authentic IDLE Shell Output Blue */
      white-space: pre-wrap;
      font-size: 13px;
      line-height: 1.38;
      background: #fdfdfd;
      border-left: 2px solid #0000ff;
      padding: 4px 8px;
      margin-top: 2px;
    }

    #no-results {
      display: none;
      color: #dd0000;
      margin: 20px 0;
      font-weight: bold;
    }

    /* Copied Toast */
    .toast {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #202124;
      color: #ffffff;
      padding: 6px 14px;
      font-family: "Segoe UI", Tahoma, sans-serif;
      font-size: 12px;
      border-radius: 3px;
      opacity: 0;
      transition: opacity 0.2s ease;
      pointer-events: none;
      box-shadow: 0 2px 8px rgba(0,0,0,0.3);
      z-index: 9999;
    }
    .toast.show {
      opacity: 1;
    }
  </style>
</head>
<body>

  <!-- Windows Classic Title Bar -->
  <div class="idle-titlebar">
    <div class="idle-title-left">
      <span class="py-icon">🐍</span>
      <span>IDLE Shell 3.14.6</span>
    </div>
    <div class="win-controls">
      <div class="win-btn" title="Minimize">—</div>
      <div class="win-btn" title="Maximize">▢</div>
      <div class="win-btn close" title="Close">✕</div>
    </div>
  </div>

  <!-- IDLE Menu Bar -->
  <div class="idle-menubar">
    <span>File</span>
    <span>Edit</span>
    <span>Shell</span>
    <span>Debug</span>
    <span>Options</span>
    <span>Window</span>
    <span>Help</span>
  </div>

  <!-- Subject Toggle Toolbar -->
  <div class="subject-toolbar">
    <span class="toolbar-label">Select Subject:</span>
    <button class="subject-btn active" id="btn-nlp" onclick="switchSubject('nlp')">
      <span>🐍</span> NLP Practicals (1 to 11)
    </button>
    <button class="subject-btn" id="btn-de" onclick="switchSubject('de')">
      <span>⚙️</span> Data Engineering (1 to 8)
    </button>
  </div>

  <!-- Main Pure IDLE Shell Canvas -->
  <div class="idle-shell-body">

    <div class="shell-intro">Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help", "copyright", "credits" or "license()" for more information.
<span class="comment-line"># Lab Practical Repository | Om Bichave | T.Y. Data Science (Sem 5)</span></div>

    <!-- Shell Interactive Search Line -->
    <div class="prompt-box">
      <div class="prompt-line">
        <span class="prompt-arrow">&gt;&gt;&gt;</span>
        <input 
          type="text" 
          id="search-input" 
          class="prompt-input" 
          placeholder="search_keyword(e.g., pos, spacy, tfidf, airflow, spark, eda, 4)..." 
          autofocus
        />
      </div>

      <!-- Quick Filter Chips -->
      <div class="filter-tags" id="nlp-filters">
        <span style="color:#555; margin-right:4px;">Filters:</span>
        <span class="tag-chip active" onclick="applyTag('all')">All</span>
        <span class="tag-chip" onclick="applyTag('token')">Tokenization</span>
        <span class="tag-chip" onclick="applyTag('clean')">Clean Data</span>
        <span class="tag-chip" onclick="applyTag('stem')">Stemming & Lemmatization</span>
        <span class="tag-chip" onclick="applyTag('pos')">POS Tagging</span>
        <span class="tag-chip" onclick="applyTag('trigram')">Trigrams</span>
        <span class="tag-chip" onclick="applyTag('spacy')">SpaCy</span>
        <span class="tag-chip" onclick="applyTag('ner')">NER</span>
        <span class="tag-chip" onclick="applyTag('spell')">SpellChecker</span>
        <span class="tag-chip" onclick="applyTag('tfidf')">TF-IDF</span>
        <span class="tag-chip" onclick="applyTag('bayes')">Naive Bayes</span>
      </div>

      <div class="filter-tags" id="de-filters" style="display: none;">
        <span style="color:#555; margin-right:4px;">Filters:</span>
        <span class="tag-chip active" onclick="applyTag('all')">All</span>
        <span class="tag-chip" onclick="applyTag('parse')">Data Parsing & Regex</span>
        <span class="tag-chip" onclick="applyTag('sql')">SQL & CRUD</span>
        <span class="tag-chip" onclick="applyTag('eda')">EDA & Outliers (IQR)</span>
        <span class="tag-chip" onclick="applyTag('api')">API & Flat File ETL</span>
        <span class="tag-chip" onclick="applyTag('airflow')">Airflow DAG</span>
        <span class="tag-chip" onclick="applyTag('incremental')">Incremental ETL</span>
        <span class="tag-chip" onclick="applyTag('pyspark')">PySpark</span>
        <span class="tag-chip" onclick="applyTag('pipeline')">End-to-End Pipeline</span>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- SECTION 1: NLP PRACTICALS (1 to 11)                      -->
    <!-- ======================================================== -->
    <div id="section-nlp">

      <!-- P1 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 1 p1 sentence segmentation word tokenization nltk punkt tokenize">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp1.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-1')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 1: Aim: To perform sentence segmentation and word tokenization on a given text using the NLTK library.</div>
        <pre class="code-box" id="nlp-code-1"><span class="kw">import</span> nltk
<span class="kw">from</span> nltk.tokenize <span class="kw">import</span> sent_tokenize, word_tokenize

nltk.download(<span class="str">'punkt'</span>)
nltk.download(<span class="str">'punkt_tab'</span>)

text = <span class="str">"Natural Language Processing (NLP) is a branch of artificial intelligence. It helps computers read, understand, and write human language."</span>

sentences = sent_tokenize(text)
<span class="builtin">print</span>(<span class="str">"Sentence Segmentation:"</span>)
<span class="kw">for</span> idx, sentence <span class="kw">in</span> <span class="builtin">enumerate</span>(sentences, 1):
    <span class="builtin">print</span>(<span class="str">f"Sentence {idx}:{sentence}"</span>)

<span class="builtin">print</span>(<span class="str">"\nWord Tokenization:"</span>)
<span class="kw">for</span> idx, sentence <span class="kw">in</span> <span class="builtin">enumerate</span>(sentences, 1):
    tokens = word_tokenize(sentence)
    <span class="builtin">print</span>(<span class="str">f"Sentence{idx}: {tokens}"</span>)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">Sentence Segmentation:
Sentence 1:Natural Language Processing (NLP) is a branch of artificial intelligence.
Sentence 2:It helps computers read, understand, and write human language.

Word Tokenization:
Sentence1: ['Natural', 'Language', 'Processing', '(', 'NLP', ')', 'is', 'a', 'branch', 'of', 'artificial', 'intelligence', '.']
Sentence2: ['It', 'helps', 'computers', 'read', ',', 'understand', ',', 'and', 'write', 'human', 'language', '.']</pre>
        </div>
      </div>

      <!-- P2 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 2 p2 clean dataset missing values duplicate records pandas dropna drop_duplicates">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp2.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-2')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 2: Aim: To clean a dataset by removing missing values and duplicate records using Pandas.</div>
        <pre class="code-box" id="nlp-code-2"><span class="kw">import</span> pandas <span class="kw">as</span> pd

df = pd.read_csv(<span class="str">"annual-enterprise-survey-2025-financial-year-provisional.csv"</span>)
<span class="builtin">print</span>(df.head())

<span class="builtin">print</span>(<span class="str">"Original Dataset:"</span>)
<span class="builtin">print</span>(df)

df = df.dropna()
df = df.drop_duplicates()

<span class="builtin">print</span>(<span class="str">"\n Cleaned Dataset:"</span>)
<span class="builtin">print</span>(df)

df.to_csv(<span class="str">"student_cleaned.csv"</span>, index=<span class="kw">False</span>)
<span class="builtin">print</span>(<span class="str">"\n Blank values and duplicate rows removed successfully."</span>)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">Cleaned Dataset:
[60255 rows x 10 columns]

Blank values and duplicate rows removed successfully.</pre>
        </div>
      </div>

      <!-- P3 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 3 p3 stemming lemmatization nltk porterstemmer wordnetlemmatizer wordnet">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp3.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-3')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 3: Aim: To perform Stemming and Lemmatization on a given sentence using the NLTK library in python.</div>
        <pre class="code-box" id="nlp-code-3"><span class="kw">import</span> nltk
<span class="kw">from</span> nltk.stem <span class="kw">import</span> PorterStemmer, WordNetLemmatizer
<span class="kw">from</span> nltk.tokenize <span class="kw">import</span> word_tokenize

nltk.download(<span class="str">'punkt'</span>)
nltk.download(<span class="str">'wordnet'</span>)
nltk.download(<span class="str">'omw-1.4'</span>)

text = <span class="str">"Do what you can, with what you have, where you are"</span>
tokens = word_tokenize(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

<span class="builtin">print</span>(<span class="str">"stemming:"</span>)
<span class="kw">for</span> word <span class="kw">in</span> tokens:
    <span class="builtin">print</span>(<span class="str">f"{word}->{stemmer.stem(word)}"</span>)

<span class="builtin">print</span>(<span class="str">"\n Lemmatization:"</span>)
<span class="kw">for</span> word <span class="kw">in</span> tokens:
    <span class="builtin">print</span>(<span class="str">f"{word}->{lemmatizer.lemmatize(word)}"</span>)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">stemming:
Do->do
what->what
you->you
can->can
,->,
with->with
what->what
you->you
have->have
,->,
where->where
you->you
are->are

Lemmatization:
Do->Do
what->what
you->you
can->can
,->,
with->with
what->what
you->you
have->have
,->,
where->where
you->you
are->are</pre>
        </div>
      </div>

      <!-- P4 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 4 p4 part-of-speech pos tagging nltk pos_tag input">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp4.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-4')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 4: Aim: Part-of-speech (POS) tagging using NLTK.</div>
        <pre class="code-box" id="nlp-code-4"><span class="kw">import</span> nltk
<span class="kw">from</span> nltk.tokenize <span class="kw">import</span> word_tokenize
<span class="kw">from</span> nltk <span class="kw">import</span> pos_tag

nltk.download(<span class="str">'punkt_tab'</span>)
nltk.download(<span class="str">'averaged_perceptron_tagger_eng'</span>)

text = <span class="builtin">input</span>(<span class="str">"Enter a sentence: "</span>)

words = word_tokenize(text)
tags = pos_tag(words)

<span class="builtin">print</span>(<span class="str">"\nPOS Tags:"</span>)
<span class="kw">for</span> word, tag <span class="kw">in</span> tags:
    <span class="builtin">print</span>(<span class="str">f"{word}--> {tag}"</span>)</pre>
        <div class="output-section">
          <div class="output-label">Sample Run:</div>
          <pre class="output-box">Enter a sentence: If you tell the truth, you do not have to remember anything

POS Tags:
If--> IN
you--> PRP
tell--> VBP
the--> DT
truth--> NN
,--> ,
you--> PRP
do--> VBP
not--> RB
have--> VB
to--> TO
remember--> VB
anything--> NN</pre>
        </div>
      </div>

      <!-- P5 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 5 p5 counting part of speech pos tags counter nltk frequency">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp5.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-5')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 5: Aim: Counting Part-of-speech (POS) tags using NLTK.</div>
        <pre class="code-box" id="nlp-code-5"><span class="kw">import</span> nltk
<span class="kw">from</span> nltk.tokenize <span class="kw">import</span> word_tokenize
<span class="kw">from</span> collections <span class="kw">import</span> Counter

nltk.download(<span class="str">'punkt'</span>)
nltk.download(<span class="str">'averaged_perceptron_tagger'</span>)

text = <span class="str">"If you tell the truth, you don't have to remember anything"</span>

tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

<span class="builtin">print</span>(<span class="str">"POS Tags:"</span>)
<span class="builtin">print</span>(pos_tags)

tags = [tag <span class="kw">for</span> word, tag <span class="kw">in</span> pos_tags]
tag_count = Counter(tags)

<span class="builtin">print</span>(<span class="str">"\nCount of POS Tags:"</span>)
<span class="kw">for</span> tag, count <span class="kw">in</span> tag_count.items():
    <span class="builtin">print</span>(<span class="str">f"{tag}:{count}"</span>)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">POS Tags:
[('If', 'IN'), ('you', 'PRP'), ('tell', 'VBP'), ('the', 'DT'), ('truth', 'NN'), (',', ','), ('you', 'PRP'), ('do', 'VBP'), ("n't", 'RB'), ('have', 'VB'), ('to', 'TO'), ('remember', 'VB'), ('anything', 'NN')]

Count of POS Tags:
IN:1
PRP:2
VBP:2
DT:1
NN:2
,:1
RB:1
VB:2
TO:1</pre>
        </div>
      </div>

      <!-- P6 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 6 p6 trigrams ngrams frequency count nltk counter">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp6.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-6')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 6: Aim: Generation of trigrams and frequency count using NLTK.</div>
        <pre class="code-box" id="nlp-code-6"><span class="kw">import</span> nltk
<span class="kw">from</span> nltk.util <span class="kw">import</span> ngrams
<span class="kw">from</span> nltk.tokenize <span class="kw">import</span> word_tokenize
<span class="kw">from</span> collections <span class="kw">import</span> Counter

nltk.download(<span class="str">'punkt'</span>)

text = <span class="str">"NLP helps computers understand human language."</span>
tokens = word_tokenize(text.lower())
trigrams = <span class="builtin">list</span>(ngrams(tokens, 3))

<span class="builtin">print</span>(<span class="str">"Generated trigrams:"</span>)
<span class="kw">for</span> trigram <span class="kw">in</span> trigrams:
    <span class="builtin">print</span>(trigram)

trigram_freq = Counter(trigrams)
<span class="builtin">print</span>(<span class="str">"\nTrigram Frequencies:"</span>)
<span class="kw">for</span> trigram, freq <span class="kw">in</span> trigram_freq.items():
    <span class="builtin">print</span>(<span class="str">f"{trigram} : {freq}"</span>)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">Generated trigrams:
('nlp', 'helps', 'computers')
('helps', 'computers', 'understand')
('computers', 'understand', 'human')
('understand', 'human', 'language')
('human', 'language', '.')

Trigram Frequencies:
('nlp', 'helps', 'computers') : 1
('helps', 'computers', 'understand') : 1
('computers', 'understand', 'human') : 1
('understand', 'human', 'language') : 1
('human', 'language', '.') : 1</pre>
        </div>
      </div>

      <!-- P7 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 7 p7 spacy pos tagging neural language model en_core_web_sm">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp77.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-7')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 7: Aim: Part-of-speech (POS) tagging using SpaCy neural language model.</div>
        <pre class="code-box" id="nlp-code-7"><span class="kw">import</span> spacy

nlp = spacy.load(<span class="str">"en_core_web_sm"</span>)

text = <span class="str">"Part-of-speech tagging labels words by their grammar."</span>
doc = nlp(text)

<span class="builtin">print</span>(<span class="str">"\nPOS Tagging using Neural Model(SpaCy):"</span>)
<span class="kw">for</span> token <span class="kw">in</span> doc:
    <span class="builtin">print</span>(<span class="str">f"{token.text}->{token.pos_}({token.tag_})"</span>)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">POS Tagging using Neural Model(SpaCy):
Part->NOUN(NN)
-->PUNCT(HYPH)
of->ADP(IN)
-->PUNCT(HYPH)
speech->NOUN(NN)
tagging->VERB(VBG)
labels->VERB(VBZ)
words->NOUN(NNS)
by->ADP(IN)
their->PRON(PRP$)
grammar->NOUN(NN)
.->PUNCT(.)</pre>
        </div>
      </div>

      <!-- P8 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 8 p8 named entity recognition ner spacy persons organizations locations dates">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp88.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-8')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 8: Aim: To perform Named Entity Recognition (NER) on a given sentence using SpaCy.</div>
        <pre class="code-box" id="nlp-code-8"><span class="kw">import</span> spacy

nlp = spacy.load(<span class="str">"en_core_web_sm"</span>)

text = <span class="builtin">input</span>(<span class="str">"Enter a sentence: "</span>)
doc = nlp(text)

<span class="kw">if</span> <span class="builtin">len</span>(doc.ents) == 0:
    <span class="builtin">print</span>(<span class="str">"\nNo Named Entity Found."</span>)
    <span class="builtin">print</span>(<span class="str">"Please enter a sentence containing a person's name, organization, place, date, etc."</span>)
<span class="kw">else</span>:
    <span class="builtin">print</span>(<span class="str">"\nNamed Entities Found:\n"</span>)
    <span class="kw">for</span> ent <span class="kw">in</span> doc.ents:
        <span class="builtin">print</span>(<span class="str">f"{ent.text}->{ent.label_}"</span>)</pre>
        <div class="output-section">
          <div class="output-label">Sample Run:</div>
          <pre class="output-box">Enter a sentence: Qin Shi Huang (February 259 - 12 July 210 BC) was the founder of the Qin dynasty and the first emperor of China

Named Entities Found:

Qin Shi Huang->PERSON
February 259->DATE
12 July->DATE
BC->ORG
Qin->PERSON
first->ORDINAL
China->GPE</pre>
        </div>
      </div>

      <!-- P9 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 9 p9 spell checking correction spellchecker pyspellchecker misspelled words">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlpp9.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-9')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 9: Aim: To implement spell checking for English text using the Spellchecker library in Python.</div>
        <pre class="code-box" id="nlp-code-9"><span class="kw">from</span> spellchecker <span class="kw">import</span> SpellChecker

spell = SpellChecker()
sentence = <span class="builtin">input</span>(<span class="str">"Enter a sentence: "</span>)
words = sentence.split()
corrected = []

<span class="kw">for</span> word <span class="kw">in</span> words:
    corrected.append(spell.correction(word))

<span class="builtin">print</span>(<span class="str">"\nOriginal Sentence:"</span>)
<span class="builtin">print</span>(sentence)
<span class="builtin">print</span>(<span class="str">"\nCorrected Sentence:"</span>)
<span class="builtin">print</span>(<span class="str">" "</span>.join(corrected))</pre>
        <div class="output-section">
          <div class="output-label">Sample Run:</div>
          <pre class="output-box">Enter a sentence: I stduy data sciencee

Original Sentence:
I stduy data sciencee

Corrected Sentence:
I study data science</pre>
        </div>
      </div>

      <!-- P10 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 10 p10 tf-idf term frequency inverse document frequency vectorization scikit-learn sklearn tfidfvectorizer">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlp10.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-10')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 10: Aim: To implement TF-IDF vectorization using the Scikit-learn library in Python.</div>
        <pre class="code-box" id="nlp-code-10"><span class="kw">from</span> sklearn.feature_extraction.text <span class="kw">import</span> TfidfVectorizer

documents = [
    <span class="str">"Data science extracts valuable insights from massive amounts of data"</span>,
    <span class="str">"It powers everyday technology like predictive algorithms."</span>,
    <span class="str">"By turning raw data into actionable strategies, it helps organizations make smarter, faster, and more evidence-based decisions."</span>
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

<span class="builtin">print</span>(<span class="str">"Feature Names:"</span>)
<span class="builtin">print</span>(vectorizer.get_feature_names_out())
<span class="builtin">print</span>(<span class="str">"\nTF-IDF Matrix:"</span>)
<span class="builtin">print</span>(tfidf_matrix.toarray())</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">Feature Names:
['algorithms' 'amounts' 'and' 'based' 'data' 'decisions' 'everyday'
 'evidence' 'extracts' 'faster' 'from' 'helps' 'insights' 'it' 'like'
 'make' 'massive' 'more' 'of' 'organizations' 'powers' 'predictive'
 'science' 'smarter' 'technology' 'valuable']

TF-IDF Matrix:
[[0.         0.28867513 0.         0.         0.57735027 0.        ...]
 [0.38988801 0.         0.         0.         0.         0.        ...]
 [0.         0.         0.30746099 0.30746099 0.         0.30746099...]]</pre>
        </div>
      </div>

      <!-- P11 -->
      <div class="practical-block" data-subject="nlp" data-keywords="practical 11 p11 text classification countvectorizer multinomial naive bayes multinomialnb scikit-learn sports education">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/nlp11.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('nlp-code-11')">Copy Code</button>
        </div>
        <div class="aim-box"># Practical 11: Aim: To implement text classification using CountVectorizer and Multinomial Naive Bayes.</div>
        <pre class="code-box" id="nlp-code-11"><span class="kw">from</span> sklearn.feature_extraction.text <span class="kw">import</span> CountVectorizer
<span class="kw">from</span> sklearn.naive_bayes <span class="kw">import</span> MultinomialNB

text = [
    <span class="str">"I like cricket"</span>,
    <span class="str">"Football is my favorite sport"</span>,
    <span class="str">"I watch cricket matches"</span>,
    <span class="str">"I like studying computer science"</span>,
    <span class="str">"Python is easy to learn"</span>,
    <span class="str">"I study mathematics"</span>
]

category = [
    <span class="str">"Sports"</span>,
    <span class="str">"Sports"</span>,
    <span class="str">"Sports"</span>,
    <span class="str">"Education"</span>,
    <span class="str">"Education"</span>,
    <span class="str">"Education"</span>
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

model = MultinomialNB()
model.fit(X, category)

sentence = <span class="builtin">input</span>(<span class="str">"Enter a sentence: "</span>)
sentence_vector = vectorizer.transform([sentence])

<span class="kw">if</span> sentence_vector.nnz == 0:
    <span class="builtin">print</span>(<span class="str">"Not trained for this data"</span>)
<span class="kw">else</span>:
    result = model.predict(sentence_vector)
    <span class="builtin">print</span>(<span class="str">"Category:"</span>, result[0])</pre>
        <div class="output-section">
          <div class="output-label">Sample Run:</div>
          <pre class="output-box">Enter a sentence: I like cricket
Category: Sports</pre>
        </div>
      </div>

    </div>

    <!-- ======================================================== -->
    <!-- SECTION 2: DATA ENGINEERING PRACTICALS (1 to 8)           -->
    <!-- ======================================================== -->
    <div id="section-de" style="display: none;">

      <!-- DE P1 -->
      <div class="practical-block" data-subject="de" data-keywords="practical 1 p1 de data parsing regex binary sql crud csv html xml json text files anomalies">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/de_p1.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('de-code-1')">Copy Code</button>
        </div>
        <div class="aim-box"># DE Practical 1: Aim: Parse Text, CSV, HTML, XML, JSON, Binary Files, RegEx matching, and Relational SQL CRUD.</div>
        <pre class="code-box" id="de-code-1"><span class="com"># --- Exercise 1: Multi-Format Data Parsing & Anomaly Inspection ---</span>
<span class="kw">import</span> json, csv, re, sqlite3
<span class="kw">import</span> pandas <span class="kw">as</span> pd

<span class="com"># 1. Parsing JSON data with anomaly check</span>
raw_json = <span class="str">'[{"id": 1, "name": "Alice", "salary": 50000}, {"id": 2, "name": "Bob", "salary": null}, {"id": 3, "name": "Charlie", "salary": -100}]'</span>
records = json.loads(raw_json)
df = pd.DataFrame(records)

<span class="builtin">print</span>(<span class="str">"--- Extracted JSON Records ---"</span>)
<span class="builtin">print</span>(df)

<span class="com"># Checking anomalies (null values or negative salaries)</span>
anomalies = df[(df[<span class="str">'salary'</span>].isna()) | (df[<span class="str">'salary'</span>] &lt; 0)]
<span class="builtin">print</span>(<span class="str">"\nAnomalies Detected:"</span>)
<span class="builtin">print</span>(anomalies)

<span class="com"># --- Exercise 2: Binary File I/O ---</span>
<span class="kw">with</span> <span class="builtin">open</span>(<span class="str">"telemetry.bin"</span>, <span class="str">"wb"</span>) <span class="kw">as</span> f:
    f.write(<span class="str">b"\xDE\xAD\xBE\xEF\x00\x01\x02\x03"</span>)

<span class="kw">with</span> <span class="builtin">open</span>(<span class="str">"telemetry.bin"</span>, <span class="str">"rb"</span>) <span class="kw">as</span> f:
    bin_data = f.read()
<span class="builtin">print</span>(<span class="str">"\nBinary Data Read:"</span>, bin_data.hex())

<span class="com"># --- Exercise 3: Regular Expressions Search & Masking ---</span>
sample_text = <span class="str">"Contact admin@college.edu or support@datacamp.org with phone 9876543210"</span>
emails = re.findall(<span class="str">r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'</span>, sample_text)
masked_text = re.sub(<span class="str">r'\d{10}'</span>, <span class="str">'[MASKED_PHONE]'</span>, sample_text)
<span class="builtin">print</span>(<span class="str">"\nExtracted Emails:"</span>, emails)
<span class="builtin">print</span>(<span class="str">"Masked String:"</span>, masked_text)

<span class="com"># --- Exercise 4: Relational Database SQL CRUD Operations ---</span>
conn = sqlite3.connect(<span class="str">":memory:"</span>)
cursor = conn.cursor()
cursor.execute(<span class="str">"CREATE TABLE students (id INT PRIMARY KEY, name TEXT, gpa REAL)"</span>)
cursor.execute(<span class="str">"INSERT INTO students VALUES (1, 'Om', 3.9), (2, 'Aryan', 3.8)"</span>)
conn.commit()

cursor.execute(<span class="str">"SELECT * FROM students"</span>)
<span class="builtin">print</span>(<span class="str">"\nSQL CRUD Read:"</span>, cursor.fetchall())</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">--- Extracted JSON Records ---
   id     name   salary
0   1    Alice  50000.0
1   2      Bob      NaN
2   3  Charlie   -100.0

Anomalies Detected:
   id     name  salary
1   2      Bob     NaN
2   3  Charlie  -100.0

Binary Data Read: deadbeef00010203

Extracted Emails: ['admin@college.edu', 'support@datacamp.org']
Masked String: Contact admin@college.edu or support@datacamp.org with phone [MASKED_PHONE]

SQL CRUD Read: [(1, 'Om', 3.9), (2, 'Aryan', 3.8)]</pre>
        </div>
      </div>

      <!-- DE P2 -->
      <div class="practical-block" data-subject="de" data-keywords="practical 2 p2 de relational etl pipeline sql mysql workbench staging transformations bi">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/de_p2.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('de-code-2')">Copy Code</button>
        </div>
        <div class="aim-box"># DE Practical 2: Aim: Design a Relational ETL Pipeline with Staging & Analytical Transformation in SQL.</div>
        <pre class="code-box" id="de-code-2"><span class="kw">import</span> sqlite3
<span class="kw">import</span> pandas <span class="kw">as</span> pd

conn = sqlite3.connect(<span class="str">":memory:"</span>)
cursor = conn.cursor()

<span class="com"># 1. Staging Schema Creation</span>
cursor.execute(<span class="str">"""
CREATE TABLE staging_sales (
    order_id INT, customer_id INT, raw_amount REAL, order_date TEXT
);
"""</span>)

<span class="com"># 2. Ingesting Raw Data</span>
raw_orders = [
    (101, 1, 1500.0, <span class="str">'2026-01-10'</span>),
    (102, 2, 450.0, <span class="str">'2026-01-11'</span>),
    (103, 1, 3200.0, <span class="str">'2026-01-15'</span>),
]
cursor.executemany(<span class="str">"INSERT INTO staging_sales VALUES (?, ?, ?, ?)"</span>, raw_orders)
conn.commit()

<span class="com"># 3. Transform & Load into Production Analytics Table</span>
cursor.execute(<span class="str">"""
CREATE TABLE analytics_sales_summary AS
SELECT 
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(raw_amount) AS total_spend,
    CASE 
        WHEN SUM(raw_amount) >= 2000 THEN 'Gold Tier'
        ELSE 'Silver Tier'
    END AS customer_tier
FROM staging_sales
GROUP BY customer_id;
"""</span>)

summary_df = pd.read_sql_query(<span class="str">"SELECT * FROM analytics_sales_summary"</span>, conn)
<span class="builtin">print</span>(<span class="str">"--- Relational ETL Analytics Report ---"</span>)
<span class="builtin">print</span>(summary_df)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">--- Relational ETL Analytics Report ---
   customer_id  total_orders  total_spend customer_tier
0            1             2       4700.0     Gold Tier
1            2             1        450.0   Silver Tier</pre>
        </div>
      </div>

      <!-- DE P3 -->
      <div class="practical-block" data-subject="de" data-keywords="practical 3 p3 de noise elimination feature selection eda variancethreshold outlier iqr boxplot histogram">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/de_p3.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('de-code-3')">Copy Code</button>
        </div>
        <div class="aim-box"># DE Practical 3: Aim: Noise Elimination (IQR Outlier Filtering), Feature Selection (VarianceThreshold), and EDA.</div>
        <pre class="code-box" id="de-code-3"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np
<span class="kw">from</span> sklearn.feature_selection <span class="kw">import</span> VarianceThreshold

<span class="com"># Sample Dataset</span>
data = {
    <span class="str">'Age'</span>: [20, 21, 22, 23, 24, 100],  <span class="com"># 100 is an outlier (noise)</span>
    <span class="str">'Marks'</span>: [75, 80, 85, 90, 95, 20],
    <span class="str">'Attendance'</span>: [85, 88, 90, 92, 94, 50],
    <span class="str">'Constant'</span>: [1, 1, 1, 1, 1, 1]  <span class="com"># Constant feature (0 variance)</span>
}

df = pd.DataFrame(data)
<span class="builtin">print</span>(<span class="str">"Original Dataset:"</span>)
<span class="builtin">print</span>(df)

<span class="com"># 1. Noise Elimination (Outlier Removal using IQR)</span>
Q1 = df[<span class="str">'Age'</span>].quantile(0.25)
Q3 = df[<span class="str">'Age'</span>].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df[<span class="str">'Age'</span>] &gt;= lower) &amp; (df[<span class="str">'Age'</span>] &lt;= upper)]
<span class="builtin">print</span>(<span class="str">"\nDataset after Noise Elimination:"</span>)
<span class="builtin">print</span>(df_clean)

<span class="com"># 2. Feature Selection (Remove constant features with 0 variance)</span>
selector = VarianceThreshold(threshold=0.0)
selected = selector.fit_transform(df_clean)
selected_columns = df_clean.columns[selector.get_support()]

<span class="builtin">print</span>(<span class="str">"\nSelected Features:"</span>)
<span class="builtin">print</span>(selected_columns)

<span class="com"># 3. Exploratory Data Analysis (EDA)</span>
<span class="builtin">print</span>(<span class="str">"\nStatistical Summary:"</span>)
<span class="builtin">print</span>(df_clean[selected_columns].describe())</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">Original Dataset:
   Age  Marks  Attendance  Constant
0   20     75          85         1
1   21     80          88         1
2   22     85          90         1
3   23     90          92         1
4   24     95          94         1
5  100     20          50         1

Dataset after Noise Elimination:
   Age  Marks  Attendance  Constant
0   20     75          85         1
1   21     80          88         1
2   22     85          90         1
3   23     90          92         1
4   24     95          94         1

Selected Features:
Index(['Age', 'Marks', 'Attendance'], dtype='object')</pre>
        </div>
      </div>

      <!-- DE P4 -->
      <div class="practical-block" data-subject="de" data-keywords="practical 4 p4 de rest api extraction flat file csv merge requests json_normalize">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/de_p4.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('de-code-4')">Copy Code</button>
        </div>
        <div class="aim-box"># DE Practical 4: Aim: Extracting Data from REST APIs and Flat Files Using Python and Staging to Warehouse.</div>
        <pre class="code-box" id="de-code-4"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> requests

<span class="kw">def</span> <span class="builtin">extract_api_data</span>(url):
    <span class="str">"""Fetches data from a REST API and returns a DataFrame."""</span>
    <span class="kw">try</span>:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        <span class="kw">return</span> pd.json_normalize(data)
    <span class="kw">except</span> Exception <span class="kw">as</span> e:
        <span class="builtin">print</span>(<span class="str">f"API Fallback: {e}"</span>)
        <span class="com"># Mock fallback if internet is restricted in lab</span>
        <span class="kw">return</span> pd.DataFrame([
            {<span class="str">"id"</span>: 1, <span class="str">"name"</span>: <span class="str">"Leanne Graham"</span>, <span class="str">"email"</span>: <span class="str">"sincere@april.biz"</span>, <span class="str">"company.name"</span>: <span class="str">"Romaguera-Crona"</span>},
            {<span class="str">"id"</span>: 2, <span class="str">"name"</span>: <span class="str">"Ervin Howell"</span>, <span class="str">"email"</span>: <span class="str">"shanna@melissa.tv"</span>, <span class="str">"company.name"</span>: <span class="str">"Deckow-Crist"</span>}
        ])

<span class="kw">def</span> <span class="builtin">extract_csv_data</span>(file_path):
    <span class="kw">return</span> pd.read_csv(file_path)

<span class="kw">if</span> __name__ == <span class="str">"__main__"</span>:
    <span class="com"># 1. API Extraction</span>
    api_url = <span class="str">"https://jsonplaceholder.typicode.com/users"</span>
    api_df = extract_api_data(api_url)
    api_df = api_df[[<span class="str">"id"</span>, <span class="str">"name"</span>, <span class="str">"email"</span>, <span class="str">"company.name"</span>]]
    api_df.rename(columns={<span class="str">"company.name"</span>: <span class="str">"company"</span>}, inplace=<span class="kw">True</span>)

    <span class="com"># 2. Flat File Creation & Extraction</span>
    csv_file = <span class="str">"locations.csv"</span>
    pd.DataFrame({
        <span class="str">"id"</span>: [1, 2],
        <span class="str">"city"</span>: [<span class="str">"New York"</span>, <span class="str">"London"</span>]
    }).to_csv(csv_file, index=<span class="kw">False</span>)

    csv_df = extract_csv_data(csv_file)

    <span class="com"># 3. Data Transformation & Merging</span>
    merged_df = pd.merge(api_df, csv_df, on=<span class="str">"id"</span>, how=<span class="str">"inner"</span>)
    <span class="builtin">print</span>(<span class="str">"--- Merged ETL Pipeline Data View ---"</span>)
    <span class="builtin">print</span>(merged_df)

    merged_df.to_csv(<span class="str">"cleaned_warehouse_profiles.csv"</span>, index=<span class="kw">False</span>)
    <span class="builtin">print</span>(<span class="str">"\nData successfully saved to 'cleaned_warehouse_profiles.csv'"</span>)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">--- Merged ETL Pipeline Data View ---
   id           name              email          company      city
0   1  Leanne Graham  sincere@april.biz  Romaguera-Crona  New York
1   2   Ervin Howell  shanna@melissa.tv     Deckow-Crist    London

Data successfully saved to 'cleaned_warehouse_profiles.csv'</pre>
        </div>
      </div>

      <!-- DE P5 -->
      <div class="practical-block" data-subject="de" data-keywords="practical 5 p5 de apache airflow dag directed acyclic graph bashoperator emptyoperator orchestration">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/de_p5_dag.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('de-code-5')">Copy Code</button>
        </div>
        <div class="aim-box"># DE Practical 5: Aim: Setting up Apache Airflow and Creating a DAG for Automated ETL Orchestration.</div>
        <pre class="code-box" id="de-code-5"><span class="kw">from</span> datetime <span class="kw">import</span> datetime, timedelta
<span class="kw">from</span> airflow <span class="kw">import</span> DAG
<span class="kw">from</span> airflow.operators.bash <span class="kw">import</span> BashOperator
<span class="kw">from</span> airflow.operators.empty <span class="kw">import</span> EmptyOperator

<span class="com"># Default arguments for workflow pipeline execution</span>
default_args = {
    <span class="str">"owner"</span>: <span class="str">"data_engineering_lab"</span>,
    <span class="str">"depends_on_past"</span>: <span class="kw">False</span>,
    <span class="str">"start_date"</span>: datetime(2026, 1, 1),
    <span class="str">"email_on_failure"</span>: <span class="kw">False</span>,
    <span class="str">"email_on_retry"</span>: <span class="kw">False</span>,
    <span class="str">"retries"</span>: 1,
    <span class="str">"retry_delay"</span>: timedelta(minutes=5),
}

<span class="com"># Define the DAG context</span>
<span class="kw">with</span> DAG(
    <span class="str">"university_etl_orchestration"</span>,
    default_args=default_args,
    description=<span class="str">"Lab assignment for API and Flat File ETL orchestration"</span>,
    schedule_interval=timedelta(days=1),
    catchup=<span class="kw">False</span>,
) <span class="kw">as</span> dag:

    <span class="com"># Task 1: Pipeline Init Anchor</span>
    start_pipeline = EmptyOperator(task_id=<span class="str">"start_pipeline"</span>)

    <span class="com"># Task 2: Run Python Extraction Script</span>
    execute_extraction = BashOperator(
        task_id=<span class="str">"run_extraction_script"</span>,
        bash_command=<span class="str">"python3 /absolute/path/to/data_extraction.py"</span>,
    )

    <span class="com"># Task 3: Finalize and Log Metrics</span>
    pipeline_complete = BashOperator(
        task_id=<span class="str">"log_pipeline_success"</span>,
        bash_command=<span class="str">'echo "ETL Execution completed successfully at $(date)"'</span>,
    )

    <span class="com"># Set Task Dependencies</span>
    start_pipeline &gt;&gt; execute_extraction &gt;&gt; pipeline_complete</pre>
        <div class="output-section">
          <div class="output-label">Airflow CLI Verification:</div>
          <pre class="output-box">$ airflow dags list | grep university_etl
university_etl_orchestration | data_engineering_lab | True | 1 day, 0:00:00

$ airflow tasks test university_etl_orchestration log_pipeline_success 2026-01-01
[INFO] Executing: echo "ETL Execution completed successfully at Tue Oct 13 12:00:00 UTC 2026"
ETL Execution completed successfully at Tue Oct 13 12:00:00 UTC 2026</pre>
        </div>
      </div>

      <!-- DE P6 -->
      <div class="practical-block" data-subject="de" data-keywords="practical 6 p6 de data validation incremental etl pipeline quarantine watermark sqlite">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/de_p6.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('de-code-6')">Copy Code</button>
        </div>
        <div class="aim-box"># DE Practical 6: Aim: Comprehensive ETL Pipeline with Data Validation & High-Watermark Incremental Loading.</div>
        <pre class="code-box" id="de-code-6"><span class="kw">import</span> sqlite3
<span class="kw">import</span> pandas <span class="kw">as</span> pd

<span class="com"># Incoming Batch Data (with some corrupt/invalid records)</span>
batch_data = pd.DataFrame([
    {<span class="str">"user_id"</span>: 101, <span class="str">"name"</span>: <span class="str">"Rohan"</span>, <span class="str">"score"</span>: 720, <span class="str">"updated_at"</span>: <span class="str">"2026-02-01 10:00:00"</span>},
    {<span class="str">"user_id"</span>: 102, <span class="str">"name"</span>: <span class="str">"Pooja"</span>, <span class="str">"score"</span>: 200, <span class="str">"updated_at"</span>: <span class="str">"2026-02-01 10:05:00"</span>}, <span class="com"># INVALID (score &lt; 300)</span>
    {<span class="str">"user_id"</span>: <span class="kw">None</span>, <span class="str">"name"</span>: <span class="str">"Amit"</span>, <span class="str">"score"</span>: 650, <span class="str">"updated_at"</span>: <span class="str">"2026-02-01 10:10:00"</span>}, <span class="com"># INVALID (id is null)</span>
    {<span class="str">"user_id"</span>: 103, <span class="str">"name"</span>: <span class="str">"Sneha"</span>, <span class="str">"score"</span>: 810, <span class="str">"updated_at"</span>: <span class="str">"2026-02-01 10:15:00"</span>},
])

<span class="com"># 1. Data Quality Validation Gate</span>
valid_condition = (batch_data[<span class="str">'user_id'</span>].notna()) &amp; (batch_data[<span class="str">'score'</span>] &gt;= 300) &amp; (batch_data[<span class="str">'score'</span>] &lt;= 850)

valid_records = batch_data[valid_condition]
quarantine_records = batch_data[~valid_condition]

<span class="builtin">print</span>(<span class="str">"Valid Records Filtered:"</span>, <span class="builtin">len</span>(valid_records))
<span class="builtin">print</span>(<span class="str">"Corrupted / Quarantined Records:"</span>, <span class="builtin">len</span>(quarantine_records))

<span class="com"># 2. Incremental High-Watermark Loading into Database</span>
conn = sqlite3.connect(<span class="str">":memory:"</span>)
cursor = conn.cursor()
cursor.execute(<span class="str">"CREATE TABLE user_warehouse (user_id INT, name TEXT, score INT, updated_at TEXT)"</span>)
cursor.execute(<span class="str">"CREATE TABLE etl_watermark (last_timestamp TEXT)"</span>)
cursor.execute(<span class="str">"INSERT INTO etl_watermark VALUES ('2026-02-01 09:00:00')"</span>)
conn.commit()

<span class="com"># Check last watermark</span>
cursor.execute(<span class="str">"SELECT last_timestamp FROM etl_watermark"</span>)
last_wm = cursor.fetchone()[0]

delta_records = valid_records[valid_records[<span class="str">'updated_at'</span>] &gt; last_wm]
delta_records.to_sql(<span class="str">"user_warehouse"</span>, conn, if_exists=<span class="str">"append"</span>, index=<span class="kw">False</span>)

<span class="builtin">print</span>(<span class="str">"\nSuccessfully loaded delta records into warehouse:"</span>)
<span class="builtin">print</span>(pd.read_sql_query(<span class="str">"SELECT * FROM user_warehouse"</span>, conn))</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">Valid Records Filtered: 2
Corrupted / Quarantined Records: 2

Successfully loaded delta records into warehouse:
   user_id   name  score           updated_at
0      101  Rohan    720  2026-02-01 10:00:00
1      103  Sneha    810  2026-02-01 10:15:00</pre>
        </div>
      </div>

      <!-- DE P7 -->
      <div class="practical-block" data-subject="de" data-keywords="practical 7 p7 de pyspark dataframes schema aggregation duplicates join sales">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/de_p7_pyspark.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('de-code-7')">Copy Code</button>
        </div>
        <div class="aim-box"># DE Practical 7: Aim: Distributed Data Processing with PySpark DataFrames (Schema, Filters, Joins, Aggregation).</div>
        <pre class="code-box" id="de-code-7"><span class="kw">from</span> pyspark.sql <span class="kw">import</span> SparkSession
<span class="kw">from</span> pyspark.sql.functions <span class="kw">import</span> col, avg

<span class="com"># 1. Initialize SparkSession</span>
spark = SparkSession.builder.appName(<span class="str">"DE_Lab_PySpark"</span>).getOrCreate()

<span class="com"># 2. Sample Datasets</span>
sales_data = [
    (1, <span class="str">"Electronics"</span>, 1500.0),
    (2, <span class="str">"Electronics"</span>, 2500.0),
    (3, <span class="str">"Clothing"</span>, 800.0),
    (3, <span class="str">"Clothing"</span>, 800.0),  <span class="com"># Duplicate row</span>
    (4, <span class="str">"Grocery"</span>, 300.0),
]
columns = [<span class="str">"sale_id"</span>, <span class="str">"category"</span>, <span class="str">"amount"</span>]
df = spark.createDataFrame(sales_data, columns)

<span class="builtin">print</span>(<span class="str">"Schema:"</span>)
df.printSchema()

<span class="com"># 3. Deduplication</span>
df_clean = df.dropDuplicates()

<span class="com"># 4. Filter & Aggregate (Average sales by category)</span>
avg_sales = df_clean.groupBy(<span class="str">"category"</span>).agg(avg(<span class="str">"amount"</span>).alias(<span class="str">"avg_sales"</span>))
<span class="builtin">print</span>(<span class="str">"\nAverage Sales by Product Category:"</span>)
avg_sales.show()</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">Schema:
root
 |-- sale_id: long (nullable = true)
 |-- category: string (nullable = true)
 |-- amount: double (nullable = true)

Average Sales by Product Category:
+-----------+---------+
|   category|avg_sales|
+-----------+---------+
|Electronics|   2000.0|
|   Clothing|    800.0|
|    Grocery|    300.0|
+-----------+---------+ </pre>
        </div>
      </div>

      <!-- DE P8 -->
      <div class="practical-block" data-subject="de" data-keywords="practical 8 p8 de end to end pipeline ecommerce data cleaning sql database reporting">
        <div class="restart-bar">
          <span class="restart-text">================================ RESTART: C:/Users/HP/Desktop/de_p8_pipeline.py ================================</span>
          <button class="copy-btn" onclick="copySnippet('de-code-8')">Copy Code</button>
        </div>
        <div class="aim-box"># DE Practical 8: Aim: Build an End-to-End Pipeline: CSV -> Python/Pandas -> Data Cleaning -> SQL Database -> Report.</div>
        <pre class="code-box" id="de-code-8"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> sqlite3

<span class="com"># 1. Extraction: Simulating Ingestion of E-Commerce Data</span>
orders_raw = pd.DataFrame({
    <span class="str">"order_id"</span>: [1001, 1002, 1003, 1004],
    <span class="str">"customer"</span>: [<span class="str">"Om"</span>, <span class="str">"Aryan"</span>, <span class="str">"Veda"</span>, <span class="str">"Unknown"</span>],
    <span class="str">"product"</span>: [<span class="str">"Laptop"</span>, <span class="str">"Headphones"</span>, <span class="str">"Mouse"</span>, <span class="str">"Keyboard"</span>],
    <span class="str">"price"</span>: [65000, 3000, <span class="kw">None</span>, 1500],  <span class="com"># Missing value</span>
    <span class="str">"status"</span>: [<span class="str">"Delivered"</span>, <span class="str">"Delivered"</span>, <span class="str">"Cancelled"</span>, <span class="str">"Pending"</span>]
})

<span class="builtin">print</span>(<span class="str">"1. Raw Ingested E-Commerce Stream:"</span>)
<span class="builtin">print</span>(orders_raw)

<span class="com"># 2. Transformation & Data Cleaning</span>
orders_clean = orders_raw.dropna(subset=[<span class="str">"price"</span>]).copy()
orders_clean = orders_clean[orders_clean[<span class="str">"status"</span>] == <span class="str">"Delivered"</span>]

<span class="com"># 3. Loading into Production SQL Database</span>
conn = sqlite3.connect(<span class="str">":memory:"</span>)
orders_clean.to_sql(<span class="str">"fact_orders"</span>, conn, index=<span class="kw">False</span>)

<span class="com"># 4. Automated BI Report Query</span>
query = <span class="str">"""
SELECT 
    COUNT(order_id) AS total_delivered_orders,
    SUM(price) AS total_revenue
FROM fact_orders;
"""</span>
report_df = pd.read_sql_query(query, conn)
<span class="builtin">print</span>(<span class="str">"\n2. Executive Financial Report Generated:"</span>)
<span class="builtin">print</span>(report_df)</pre>
        <div class="output-section">
          <div class="output-label">Output:</div>
          <pre class="output-box">1. Raw Ingested E-Commerce Stream:
   order_id customer     product    price     status
0      1001       Om      Laptop  65000.0  Delivered
1      1002    Aryan  Headphones   3000.0  Delivered
2      1003     Veda       Mouse      NaN  Cancelled
3      1004  Unknown    Keyboard   1500.0    Pending

2. Executive Financial Report Generated:
   total_delivered_orders  total_revenue
0                       2        68000.0</pre>
        </div>
      </div>

    </div>

    <!-- Error message for no matches -->
    <div id="no-results">
      Traceback (most recent call last):<br>
      NameError: name 'no_matching_practicals' is not defined. No practical matches your search keyword.
    </div>

  </div>

  <div class="toast" id="toast">Code copied to clipboard!</div>

  <script>
    let currentSubject = 'nlp';
    const searchInput = document.getElementById('search-input');
    const noResults = document.getElementById('no-results');

    function switchSubject(subj) {
      currentSubject = subj;
      document.getElementById('btn-nlp').classList.toggle('active', subj === 'nlp');
      document.getElementById('btn-de').classList.toggle('active', subj === 'de');
      
      document.getElementById('section-nlp').style.display = (subj === 'nlp') ? 'block' : 'none';
      document.getElementById('section-de').style.display = (subj === 'de') ? 'block' : 'none';
      
      document.getElementById('nlp-filters').style.display = (subj === 'nlp') ? 'flex' : 'none';
      document.getElementById('de-filters').style.display = (subj === 'de') ? 'flex' : 'none';

      searchInput.value = '';
      applyTag('all');
    }

    function filterPracticals(query) {
      const q = query.trim().toLowerCase();
      const currentContainer = (currentSubject === 'nlp') ? document.getElementById('section-nlp') : document.getElementById('section-de');
      const blocks = currentContainer.querySelectorAll('.practical-block');
      let visible = 0;

      blocks.forEach(block => {
        const keywords = block.getAttribute('data-keywords') || '';
        const text = block.innerText.toLowerCase();

        if (!q || keywords.includes(q) || text.includes(q)) {
          block.style.display = 'block';
          visible++;
        } else {
          block.style.display = 'none';
        }
      });

      noResults.style.display = (visible === 0) ? 'block' : 'none';
    }

    searchInput.addEventListener('input', (e) => {
      // Clear active chip
      const activeFilterContainer = (currentSubject === 'nlp') ? document.getElementById('nlp-filters') : document.getElementById('de-filters');
      activeFilterContainer.querySelectorAll('.tag-chip').forEach(c => c.classList.remove('active'));
      filterPracticals(e.target.value);
    });

    function applyTag(tag) {
      const activeFilterContainer = (currentSubject === 'nlp') ? document.getElementById('nlp-filters') : document.getElementById('de-filters');
      activeFilterContainer.querySelectorAll('.tag-chip').forEach(c => c.classList.remove('active'));
      
      if (event && event.target && event.target.classList.contains('tag-chip')) {
        event.target.classList.add('active');
      }

      if (tag === 'all') {
        searchInput.value = '';
        filterPracticals('');
      } else {
        searchInput.value = tag;
        filterPracticals(tag);
      }
    }

    function copySnippet(elementId) {
      const el = document.getElementById(elementId);
      if (!el) return;
      const text = el.innerText;
      navigator.clipboard.writeText(text).then(() => {
        showToast("Code copied to clipboard!");
      }).catch(() => {
        const ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast("Code copied to clipboard!");
      });
    }

    function showToast(msg) {
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => { t.classList.remove('show'); }, 1800);
    }
  </script>
</body>
</html>
