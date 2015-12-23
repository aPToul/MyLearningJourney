from wordcloud import WordCloud

clusters = [
	#"distribution probability random distributions function parameter prior variables variable binomial beta dirichlet cumulative posterior gamma",
	#"function loss functions complex derivative exponential series gamma integral differentiable real theorem riemann sigmoid zeta",
	#"prime primes conjecture integers polynomials numbers number polynomial twin irreducible theorem integer positive fibonacci ring",
	#"document documents query search retrieval relevant recall text precision word term queries information index",
	#"quantum information state entropy classical qubit states qubits measurement bits theory neumann field alice annealing",
	#"deviation standard sample mean variance population error normal estimator estimate deviations size unbiased samples square",
	#"tobit model censored variable type tobin regression models james heckman latent econometrics likelihood censoring hours",
	#"hypothesis null test power false sample tests variances effect chi-square statistical error testing significance t-test",
	"verb auxiliary english noun adjectives speech languages modality word",
	"data algorithm matrix model learning training problem vector method regression linear space algorithms models"
]

k = 1
for cluster in clusters:
	# Generate word cloud
	wordcloud = WordCloud(relative_scaling=0, width=1600, height=1200).generate(cluster)
	wordcloud.to_file("topic_cluster_"+str(k)+".png")
	k = k + 1