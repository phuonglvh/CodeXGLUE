# Prerequisite

```bash
pip install tree_sitter
(cd parser; bash build.sh)
```

## Usages

```bash
python calc_code_bleu.py --refs reference_files --hyp candidate_file --lang java ( or c_sharp) --params 0.25,0.25,0.25,0.25(default)
```

## Examples

```bash
python calc_code_bleu.py \
    --refs ../references.txt \
    --hyp ../predictions.txt \
    --lang java \
    --params 0.25,0.25,0.25,0.25
# ngram match: 0.6075, weighted ngram match: 0.6368, syntax_match: 0.7511, dataflow_match: 0.7345
# CodeBLEU score: 0.6825
```