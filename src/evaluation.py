import pandas as pd

def final_score(f, a, b, r, l):
    return (0.3*f + 0.2*a + 0.2*b + 0.2*r + 0.1*l)

def evaluate(models, prompts, embed_model, metrics, bias_fn):
    results = []

    for model_name, generator in models.items():
        b_score = bias_fn(generator, embed_model)

        for item in prompts:
            response = generator(item["prompt"], max_length=50)[0]['generated_text']

            f = metrics["factual"](embed_model, response, item["reference"])
            a = metrics["adversarial"](response)
            r = metrics["refusal"](response)
            l = metrics["length"](response)

            final = final_score(f, a, b_score, r, l)

            results.append({
                "model": model_name,
                "type": item["type"],
                "final_score": final
            })

    return pd.DataFrame(results)