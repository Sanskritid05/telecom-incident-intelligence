function Header() {

  return (

    <header className="fixed top-0 left-[220px] right-[280px] h-[70px] bg-[#081726]/90 backdrop-blur-xl border-b border-cyan-400/20 flex items-center justify-between px-8 z-50">

      <h1 className="text-2xl font-bold tracking-wide">

        TELECOM INCIDENT INTELLIGENCE DASHBOARD

      </h1>

      <div className="flex gap-4">

        <div className="bg-[#0B1B2B] px-4 py-2 rounded-xl border border-cyan-400/20">

          Threat Level: Medium

        </div>

        <div className="bg-[#0B1B2B] mr-3 px-4 py-2 rounded-xl border border-cyan-400/20">

          Uptime: 99.9%

        </div>

      </div>

    </header>
  )
}

export default Header