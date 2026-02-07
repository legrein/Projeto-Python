import { Button } from "@/components/ui/button";
import { ArrowRight, CheckCircle2, Users, Zap, Shield, TrendingUp } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col bg-background">
      {/* Navigation */}
      <nav className="sticky top-0 z-50 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 border-b border-border">
        <div className="container flex h-16 items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center">
              <span className="text-primary-foreground font-bold text-sm">KS</span>
            </div>
            <span className="font-bold text-lg hidden sm:inline">Tech Solutions</span>
          </div>
          <div className="flex items-center gap-4">
            <a href="#servicos" className="text-sm font-medium hover:text-primary transition-colors">Serviços</a>
            <a href="#sobre" className="text-sm font-medium hover:text-primary transition-colors">Sobre</a>
            <Button size="sm">Contacte-nos</Button>
          </div>
        </div>
      </nav>

      <main className="flex-1">
        {/* Hero Section */}
        <section className="relative py-20 md:py-32 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-primary/10 via-transparent to-transparent"></div>
          <div className="container relative">
            <div className="grid md:grid-cols-2 gap-12 items-center">
              <div className="space-y-8">
                <div className="space-y-4">
                  <h1 className="text-4xl md:text-5xl font-bold tracking-tight">
                    Gestão de TI Integrada para PMEs
                  </h1>
                  <p className="text-xl text-muted-foreground max-w-lg">
                    Duas marcas complementares: <strong>kalTech</strong> para continuidade operacional e <strong>Soul IT</strong> para experiência do utilizador.
                  </p>
                </div>
                <div className="flex flex-col sm:flex-row gap-4">
                  <Button size="lg" className="gap-2">
                    Agende uma Reunião <ArrowRight className="w-4 h-4" />
                  </Button>
                  <Button size="lg" variant="outline">
                    Saiba Mais
                  </Button>
                </div>
              </div>
              <div className="relative h-96 bg-gradient-to-br from-primary/20 to-accent/20 rounded-2xl flex items-center justify-center">
                <div className="text-center space-y-4">
                  <div className="text-6xl font-bold text-primary/20">KS</div>
                  <p className="text-muted-foreground">Transformando a TI para PMEs</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Serviços Section */}
        <section id="servicos" className="py-20 bg-muted/50">
          <div className="container space-y-12">
            <div className="text-center space-y-4 max-w-2xl mx-auto">
              <h2 className="text-3xl md:text-4xl font-bold">Nossos Serviços</h2>
              <p className="text-lg text-muted-foreground">
                Soluções completas de TI, Web e Automação num único parceiro de confiança.
              </p>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
              {/* Serviço 1 */}
              <div className="bg-background rounded-xl p-8 border border-border hover:border-primary/50 transition-colors">
                <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
                  <Shield className="w-6 h-6 text-primary" />
                </div>
                <h3 className="text-xl font-bold mb-3">Suporte & Segurança</h3>
                <p className="text-muted-foreground mb-4">
                  Monitorização 24/7, backup 3-2-1, segurança de endpoint e suporte proativo N1/N2 com SLA garantido.
                </p>
                <ul className="space-y-2 text-sm">
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>SLA 4h/8h garantido</span>
                  </li>
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>Backup com testes mensais</span>
                  </li>
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>Relatórios mensais KPIs</span>
                  </li>
                </ul>
              </div>

              {/* Serviço 2 */}
              <div className="bg-background rounded-xl p-8 border border-border hover:border-primary/50 transition-colors">
                <div className="w-12 h-12 bg-accent/10 rounded-lg flex items-center justify-center mb-4">
                  <Users className="w-6 h-6 text-accent" />
                </div>
                <h3 className="text-xl font-bold mb-3">Modern Workplace</h3>
                <p className="text-muted-foreground mb-4">
                  Otimização de ferramentas de colaboração, formação contínua e suporte humanizado focado na experiência.
                </p>
                <ul className="space-y-2 text-sm">
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-accent flex-shrink-0 mt-0.5" />
                    <span>Micro-learning (15-30 min)</span>
                  </li>
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-accent flex-shrink-0 mt-0.5" />
                    <span>Medição de CSAT</span>
                  </li>
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-accent flex-shrink-0 mt-0.5" />
                    <span>SSO e MFA inteligente</span>
                  </li>
                </ul>
              </div>

              {/* Serviço 3 */}
              <div className="bg-background rounded-xl p-8 border border-border hover:border-primary/50 transition-colors">
                <div className="w-12 h-12 bg-green-500/10 rounded-lg flex items-center justify-center mb-4">
                  <Zap className="w-6 h-6 text-green-600" />
                </div>
                <h3 className="text-xl font-bold mb-3">Web & Automação</h3>
                <p className="text-muted-foreground mb-4">
                  Websites responsivos, e-commerce, integrações e automações em Python para reduzir tarefas repetitivas.
                </p>
                <ul className="space-y-2 text-sm">
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-green-600 flex-shrink-0 mt-0.5" />
                    <span>Websites responsivos</span>
                  </li>
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-green-600 flex-shrink-0 mt-0.5" />
                    <span>E-commerce integrado</span>
                  </li>
                  <li className="flex gap-2 items-start">
                    <CheckCircle2 className="w-4 h-4 text-green-600 flex-shrink-0 mt-0.5" />
                    <span>Automações Python</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        {/* Planos Section */}
        <section className="py-20">
          <div className="container space-y-12">
            <div className="text-center space-y-4 max-w-2xl mx-auto">
              <h2 className="text-3xl md:text-4xl font-bold">Planos de Preços</h2>
              <p className="text-lg text-muted-foreground">
                Escolha o plano que melhor se adequa ao seu negócio. Sem contratos de longa duração.
              </p>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
              {/* Plano Starter */}
              <div className="bg-background rounded-xl border border-border p-8 flex flex-col">
                <h3 className="text-2xl font-bold mb-2">Starter</h3>
                <p className="text-muted-foreground mb-6">Para micro-empresas</p>
                <div className="mb-6">
                  <span className="text-4xl font-bold">€150</span>
                  <span className="text-muted-foreground">/mês</span>
                </div>
                <ul className="space-y-3 mb-8 flex-1">
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>10 tickets remotos/mês</span>
                  </li>
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>Monitorização básica</span>
                  </li>
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>1 visita/trimestre</span>
                  </li>
                </ul>
                <Button variant="outline" className="w-full">Começar</Button>
              </div>

              {/* Plano Business */}
              <div className="bg-primary text-primary-foreground rounded-xl border border-primary p-8 flex flex-col relative">
                <div className="absolute top-4 right-4 bg-accent text-accent-foreground px-3 py-1 rounded-full text-xs font-bold">
                  Recomendado
                </div>
                <h3 className="text-2xl font-bold mb-2">Business</h3>
                <p className="text-primary-foreground/80 mb-6">Para PMEs em crescimento</p>
                <div className="mb-6">
                  <span className="text-4xl font-bold">€350</span>
                  <span className="text-primary-foreground/80">/mês</span>
                </div>
                <ul className="space-y-3 mb-8 flex-1">
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 flex-shrink-0 mt-0.5" />
                    <span>Backups geridos</span>
                  </li>
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 flex-shrink-0 mt-0.5" />
                    <span>Gestão de endpoints</span>
                  </li>
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 flex-shrink-0 mt-0.5" />
                    <span>2 visitas/mês</span>
                  </li>
                </ul>
                <Button variant="secondary" className="w-full">Começar</Button>
              </div>

              {/* Plano Enterprise */}
              <div className="bg-background rounded-xl border border-border p-8 flex flex-col">
                <h3 className="text-2xl font-bold mb-2">Enterprise</h3>
                <p className="text-muted-foreground mb-6">Para PMEs consolidadas</p>
                <div className="mb-6">
                  <span className="text-4xl font-bold">€650</span>
                  <span className="text-muted-foreground">/mês</span>
                </div>
                <ul className="space-y-3 mb-8 flex-1">
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>Gestão de rede completa</span>
                  </li>
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>Relatórios mensais KPIs</span>
                  </li>
                  <li className="flex gap-2 items-start text-sm">
                    <CheckCircle2 className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    <span>Suporte 24/7 dedicado</span>
                  </li>
                </ul>
                <Button variant="outline" className="w-full">Começar</Button>
              </div>
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="py-20 bg-primary text-primary-foreground">
          <div className="container text-center space-y-8">
            <div className="space-y-4">
              <h2 className="text-3xl md:text-4xl font-bold">Pronto para Transformar a Sua TI?</h2>
              <p className="text-lg text-primary-foreground/80 max-w-2xl mx-auto">
                Contacte-nos hoje para uma auditoria inicial gratuita e conheça como podemos ajudar o seu negócio.
              </p>
            </div>
            <Button size="lg" variant="secondary" className="gap-2">
              Agende uma Reunião <ArrowRight className="w-4 h-4" />
            </Button>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-border bg-muted/50 py-12">
        <div className="container">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div className="space-y-4">
              <h4 className="font-bold">Tech Solutions</h4>
              <p className="text-sm text-muted-foreground">Gestão de TI integrada para PMEs em Portugal.</p>
            </div>
            <div className="space-y-4">
              <h4 className="font-bold">Serviços</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground transition-colors">Suporte & Segurança</a></li>
                <li><a href="#" className="hover:text-foreground transition-colors">Modern Workplace</a></li>
                <li><a href="#" className="hover:text-foreground transition-colors">Web & Automação</a></li>
              </ul>
            </div>
            <div className="space-y-4">
              <h4 className="font-bold">Empresa</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground transition-colors">Sobre Nós</a></li>
                <li><a href="#" className="hover:text-foreground transition-colors">Blog</a></li>
                <li><a href="#" className="hover:text-foreground transition-colors">Contacto</a></li>
              </ul>
            </div>
            <div className="space-y-4">
              <h4 className="font-bold">Contacto</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li>contacto@techsolutions.pt</li>
                <li>+351 XXX XXX XXX</li>
                <li>www.techsolutions.pt</li>
              </ul>
            </div>
          </div>
          <div className="border-t border-border pt-8 text-center text-sm text-muted-foreground">
            <p>&copy; 2026 Tech Solutions. Todos os direitos reservados.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
