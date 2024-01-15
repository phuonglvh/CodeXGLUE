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
# ngram match: 0.6075256576979613, weighted ngram match: 0.6367970871812899, syntax_match: 0.7511111111111111, dataflow_match: 0.7256637168141593
CodeBLEU score:  0.6802743932011304
```